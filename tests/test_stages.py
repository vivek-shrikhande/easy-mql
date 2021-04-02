from pyparsing import ParseException
from pytest import raises

from easymql.datatypes.primary import (
    Integer,
)
from easymql.stages import Stages, CollectionName


class TestStages:
    def test_collection_name(self):
        # with whitespace but quotes surrounded
        assert CollectionName.parse("'coll with whitespace'") == 'coll with whitespace'
        # no whitespace, no quotes surrounded
        assert (
            CollectionName.parse("coll_without_whitespace") == 'coll_without_whitespace'
        )
        # whitespace with no quotes surrounded
        with raises(ParseException):
            CollectionName.parse('coll with whitespace')
        # multiline
        with raises(ParseException):
            CollectionName.parse(
                """'coll
            with
            multiline'"""
            )
        # newline
        assert CollectionName.parse(r'coll_with\n') == r'coll_with\n'

    def test_add_fields(self):
        assert Stages.parse('ADD FIELDS "item" AS _id, "fruit" AS item;') == {
            '$addFields': {'_id': 'item', 'item': 'fruit'}
        }
        assert Stages.parse(
            'ADD FIELDS "sumScore" AS totalScore, "sumQuiz" AS totalQuizScore;'
        ) == {'$addFields': {'totalScore': 'sumScore', 'totalQuizScore': 'sumQuiz'}}
        assert Stages.parse('ADD FIELDS 1+3 AS totalScore;') == {
            '$addFields': {'totalScore': {"$add": [1, 3]}}
        }
        with raises(ParseException):
            Stages.parse('ADD FIELDS ;')  # Ask

    def test_count(self):
        assert Stages.parse('COUNT AS passing_Score;') == {'$count': 'passing_Score'}
        with raises(ParseException):
            Stages.parse('COUNT AS ;')

    def test_limit(self):
        assert Stages.parse('LIMIT 50;') == {'$limit': Integer(50)}
        with raises(ParseException):
            Stages.parse('LIMIT a;')
        with raises(ParseException):
            Stages.parse('LIMIT ;')

    def test_lookup(self):
        assert Stages.parse("LOOKUP inventory ON 'item' = 'sku';") == {
            '$lookup': {
                'from': 'inventory',
                'localField': 'item',
                'foreignField': 'sku',
                'as': 'inventory_docs',
            }
        }
        assert Stages.parse("LOOKUP inventory ON 'item' = 'sku' AS 'inventories';") == {
            '$lookup': {
                'from': 'inventory',
                'localField': 'item',
                'foreignField': 'sku',
                'as': 'inventories',
            }
        }

    def test_match(self):
        assert Stages.parse('MATCH \'author\' = "dave";') == {
            '$match': {'$expr': {'$eq': ['$author', 'dave']}}
        }
        assert Stages.parse("MATCH 'score' > 20 OR 'score' < 90;") == {
            '$match': {
                '$expr': {
                    '$or': [
                        {'$gt': ['$score', Integer(20)]},
                        {'$lt': ['$score', Integer(90)]},
                    ]
                }
            }
        }
        with raises(ParseException):
            Stages.parse('MATCH ;')

    def test_sample(self):
        assert Stages.parse('SAMPLE 23;') == {'$sample': Integer(23)}
        with raises(ParseException):
            Stages.parse('SAMPLE a;')
        with raises(ParseException):
            Stages.parse('SAMPLE ;')

    def test_skip(self):
        assert Stages.parse('OFFSET 30;') == {'$skip': Integer(30)}
        assert Stages.parse('SKIP 30;') == {'$skip': Integer(30)}
        with raises(ParseException):
            Stages.parse('OFFSET a;')
        with raises(ParseException):
            Stages.parse('SKIP ;')

    def test_sort(self):
        assert Stages.parse("SORT BY 'field1' ASC;") == {'$sort': {'field1': 1}}
        assert Stages.parse("SORT BY 'field1' DESC;") == {'$sort': {'field1': -1}}
        assert Stages.parse("SORT BY 'field1' ASC, 'field2' DESC;") == {
            '$sort': {'field1': 1, 'field2': -1}
        }
        with raises(ParseException):
            Stages.parse('SORT BY field1 BY 1, field BY -1;')
        with raises(ParseException):
            Stages.parse('SORT BY;')

    def test_sort_by_count(self):
        assert Stages.parse("SORT BY COUNT 'size';") == {'$sortByCount': '$size'}
        with raises(ParseException):
            Stages.parse('SORT BY COUNT;')
