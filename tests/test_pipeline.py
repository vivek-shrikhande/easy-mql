from easymql.pipeline import Pipeline, encode
from easymql.datatypes.primary import *


def test_encode():
    assert encode(Boolean(False)) is False
    assert encode(Boolean(True)) is True
    assert encode(Date(2021, 1, 15, 12, 30, 59, 932, '-12:00')) == {
        '$dateFromParts': {
            'year': 2021,
            'month': 1,
            'day': 15,
            'hour': 12,
            'minute': 30,
            'second': 59,
            'millisecond': 932,
            'timezone': '-12:00',
        }
    }
    assert encode(Decimal(1.2)) == 1.2
    assert encode(Integer(1)) == 1
    assert encode(Null(None)) is None
    assert encode(String("hello")) == "hello"
    assert encode([
        Integer(1),
        Integer(2),
        Integer(3),
        Null(None),
        [[]],
        [Decimal(1.2)],
        {},
        {"a": []},
        {"a": {"b": 2}},
        {"a": 1},
        2
    ]) == [1, 2, 3, None, [[]], [1.2], {}, {'a': []}, {'a': {'b': 2}}, {'a': 1}, 2]


class TestPipeline:
    def test_comments(self):
        # Single line comment
        assert Pipeline.parse(
            '''
            # filter by region
            MATCH region = "West";
            '''
        ) == {'$match': {'$expr': {'$eq': ['$region', 'West']}}}
        # Multiline line comment
        assert Pipeline.parse(
            '''
            # filter
            # by region
            MATCH region = "West";
            '''
        ) == {'$match': {'$expr': {'$eq': ['$region', 'West']}}}
        # Quick comments
        assert Pipeline.parse(
            '''
            MATCH region = "West";  # filter by region
            '''
        ) == {'$match': {'$expr': {'$eq': ['$region', 'West']}}}
        assert Pipeline.parse(
            '''
            MATCH price > 1000 +  # base price
            18 / 100;  # tax
            '''
        ) == {
            '$match': {
                '$expr': {'$gt': ['$price', {'$add': [1000, {'$divide': [18, 100]}]}]}
            }
        }
        # All mixed
        assert Pipeline.parse(
            r'''
            MATCH (name = "hello \"#world" # comment
            # full line comment
            AND (age = 10
            + # 2
            2)
            AND
            (SUBTRACT(5,
            4
            ))); COUNT
             AS doc_count;
            '''
        ) == [
            {
                '$match': {
                    '$expr': {
                        '$and': [
                            {'$eq': ['$name', 'hello "#world']},
                            {'$eq': ['$age', {'$add': [10, 2]}]},
                            {'$subtract': [5, 4]},
                        ]
                    }
                }
            },
            {'$count': 'doc_count'},
        ]
