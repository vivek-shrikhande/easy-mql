from pyparsing import ParseException
from pytest import raises

from easymql.datatypes.primary import Integer, Boolean, Decimal, String, Null
from easymql.stages import Stages, CollectionName, Field, DbName, DbCollectionPath


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
        # newline but no quotes surrounding
        with raises(ParseException):
            CollectionName.parse('coll_with\nnewline')
        # newline with quotes surrounding
        assert CollectionName.parse("'coll_with\\nnewline'") == 'coll_with\nnewline'

    def test_db_name(self):
        # with whitespace but quotes surrounded
        assert DbName.parse("'dbname with whitespace'") == 'dbname with whitespace'
        # no whitespace, no quotes surrounded
        assert DbName.parse("dbname_without_whitespace") == 'dbname_without_whitespace'
        # whitespace with no quotes surrounded
        with raises(ParseException):
            DbName.parse('dbname with whitespace')
        # multiline
        with raises(ParseException):
            DbName.parse(
                """'dbname
                with
                multiline'"""
            )
        # newline but no quotes surrounding
        with raises(ParseException):
            DbName.parse('dbname_with\nnewline')
        # newline with quotes surrounding
        assert DbName.parse("'dbname_with\\nnewline'") == 'dbname_with\nnewline'

    def test_field(self):
        # with whitespace but quotes surrounded
        assert Field.parse("'field with whitespace'") == 'field with whitespace'
        # no whitespace, no quotes surrounded
        assert Field.parse("field_without_whitespace") == 'field_without_whitespace'
        # whitespace with no quotes surrounded
        with raises(ParseException):
            Field.parse('field with whitespace')
        # multiline
        with raises(ParseException):
            Field.parse(
                """'field
                with
                multiline'"""
            )
        # newline but no quotes surrounding
        with raises(ParseException):
            Field.parse('field_with\nnewline')
        # newline with quotes surrounding
        assert Field.parse("'field_with\\nnewline'") == 'field_with\nnewline'

    def test_db_collection_path(self):
        assert DbCollectionPath.parse('DB my_db COLL my_collection') == {
            'db': 'my_db',
            'coll': 'my_collection',
        }
        assert DbCollectionPath.parse('COLL my_collection') == 'my_collection'
        with raises(ParseException):
            DbCollectionPath.parse('DB my_db')

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
            Stages.parse('ADD FIELDS ;')

    def test_count(self):
        assert Stages.parse("COUNT AS passing_Score;") == {'$count': 'passing_Score'}
        assert Stages.parse("COUNT AS 'passing_Score';") == {'$count': 'passing_Score'}
        with raises(ParseException):
            Stages.parse('COUNT AS ;')

    def test_limit(self):
        assert Stages.parse('LIMIT 50;') == {'$limit': Integer(50)}
        assert Stages.parse('LIMIT 5.0;') == {'$limit': Decimal(5.0)}
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

    def test_output_to_db(self):
        assert Stages.parse("OUTPUT TO COLL author;") == {'$out': 'author'}
        assert Stages.parse("OUTPUT TO COLL 'author';") == {'$out': 'author'}
        assert Stages.parse('OUTPUT TO COLL _author;') == {'$out': '_author'}
        assert Stages.parse("OUTPUT TO DB reporting COLL 'author';") == {
            '$out': {'db': 'reporting', 'coll': 'author'}
        }
        with raises(ParseException):
            Stages.parse('OUTPUT TO DB ;')
        with raises(ParseException):
            Stages.parse('OUTPUT TO COLL ;')

    def test_project(self):
        # no projections
        with raises(ParseException):
            Stages.parse("PROJECT ;")
        # one projection
        assert Stages.parse("PROJECT title;") == {'$project': {'title': 1}}
        # multiple projection
        assert Stages.parse("PROJECT title, author;") == {
            '$project': {'title': 1, 'author': 1}
        }
        # embedded projection
        assert Stages.parse("PROJECT author.first;") == {
            '$project': {'author.first': 1}
        }
        # exclusion
        assert Stages.parse("PROJECT - title;") == {'$project': {'title': 0}}
        assert Stages.parse("PROJECT - '-title';") == {'$project': {'-title': 0}}
        # inclusion
        assert Stages.parse("PROJECT + title;") == {'$project': {'title': 1}}
        assert Stages.parse("PROJECT + '-title';") == {'$project': {'-title': 1}}
        # add new field
        assert Stages.parse("PROJECT author.first AS first_name;") == {
            '$project': {'first_name': '$author.first'}
        }
        # all combined
        assert Stages.parse(
            "PROJECT +title, -publisher, author.first AS first_name;"
        ) == {'$project': {'title': 1, 'publisher': 0, 'first_name': '$author.first'}}
        # others
        with raises(ParseException):
            Stages.parse("PROJECT +-title;")

    def test_redact(self):
        assert Stages.parse('REDACT IF (true, "it\'s true", "it\'s false");') == {
            '$redact': {
                '$cond': {
                    'if': Boolean(True),
                    'then': String("it's true"),
                    'else': String("it's false"),
                }
            }
        }
        assert Stages.parse('REDACT IF_NULL(null, 0);') == {
            '$redact': {'$ifNull': [Null(None), Integer(0)]}
        }
        with raises(ParseException):
            Stages.parse('REDACT ;')

    def test_replace_root(self):
        assert Stages.parse(
            'REPLACE ROOT MERGE_OBJECTS({"_id": "$_id", "first":"", "last":""}, "$name");'
        ) == {
            '$replaceRoot': {
                'newRoot': {
                    '$mergeObjects': [
                        {
                            '_id': String('$_id'),
                            'first': String(''),
                            'last': String(''),
                        },
                        String('$name'),
                    ]
                }
            }
        }
        assert Stages.parse('REPLACE ROOT name;') == {
            "$replaceRoot": {"newRoot": "$name"}
        }
        assert Stages.parse('REPLACE ROOT last_name;') == {
            "$replaceRoot": {"newRoot": "$last_name"}
        }
        with raises(ParseException):
            Stages.parse('REPLACE ROOT ;')

    def test_replace_with(self):
        assert Stages.parse('REPLACE WITH MERGE_OBJECTS({"a": 1}, null);') == {
            '$replaceWith': {'$mergeObjects': [{'a': Integer(1)}, Null(None)]}
        }
        assert Stages.parse('REPLACE WITH name;') == {'$replaceWith': '$name'}
        assert Stages.parse('REPLACE WITH document_name;') == {
            '$replaceWith': '$document_name'
        }
        with raises(ParseException):
            Stages.parse('REPLACE WITH ;')

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

    def test_unset(self):
        assert Stages.parse("UNSET 'isbn';") == {'$unset': ['isbn']}
        assert Stages.parse("UNSET 'isbn', 'copies';") == {'$unset': ['isbn', 'copies']}
        assert Stages.parse("UNSET 'isbn', 'copies', 'num';") == {
            '$unset': ['isbn', 'copies', 'num']
        }
        with raises(ParseException):
            Stages.parse('UNSET ;')

    def test_unwind(self):
        # no field path
        with raises(ParseException):
            Stages.parse("UNWIND ;")
        # with field path
        assert Stages.parse("UNWIND sizes;") == {'$unwind': {'path': '$sizes'}}
        # with ARRAY INDEX AS option
        assert Stages.parse("UNWIND sizes ARRAY INDEX AS arrayIndex;") == {
            '$unwind': {'path': '$sizes', 'includeArrayIndex': 'arrayIndex'}
        }
        # with PRESERVE NULL EMPTY ARRAYS option
        assert Stages.parse("UNWIND sizes PRESERVE NULL EMPTY ARRAYS true;") == {
            '$unwind': {'path': '$sizes', 'preserveNullAndEmptyArrays': True}
        }
        # both the options
        assert Stages.parse(
            "UNWIND sizes ARRAY INDEX AS arrayIndex PRESERVE NULL EMPTY ARRAYS true;"
        ) == {
            '$unwind': {
                'path': '$sizes',
                'includeArrayIndex': 'arrayIndex',
                'preserveNullAndEmptyArrays': True,
            }
        }
        assert Stages.parse(
            "UNWIND sizes PRESERVE NULL EMPTY ARRAYS true ARRAY INDEX AS arrayIndex;"
        ) == {
            '$unwind': {
                'path': '$sizes',
                'includeArrayIndex': 'arrayIndex',
                'preserveNullAndEmptyArrays': True,
            }
        }
        # same option twice
        with raises(ParseException):
            assert Stages.parse(
                "UNWIND sizes ARRAY INDEX AS arrayIndex ARRAY INDEX AS arrayIndex;"
            )
        with raises(ParseException):
            assert Stages.parse(
                "UNWIND sizes PRESERVE NULL EMPTY ARRAYS true PRESERVE NULL EMPTY ARRAYS true;"
            )
        # missing option value
        with raises(ParseException):
            Stages.parse("UNWIND sizes ARRAY INDEX AS PRESERVE NULL EMPTY ARRAYS true;")

    def test_merge(self):
        # minimal
        assert Stages.parse('MERGE INTO COLL mycoll ;') == {
            '$merge': {'into': 'mycoll'}
        }
        assert Stages.parse('MERGE INTO DB mydb COLL mycoll ;') == {
            '$merge': {'into': {'db': 'mydb', 'coll': 'mycoll'}}
        }
        # with WHEN MATCHED clause
        # REPLACE
        assert Stages.parse(
            'MERGE INTO DB mydb COLL mycoll ' 'WHEN MATCHED THEN REPLACE;'
        ) == {
            '$merge': {
                'into': {'coll': 'mycoll', 'db': 'mydb'},
                'whenMatched': 'replace',
            }
        }
        # KEEP
        assert Stages.parse(
            'MERGE INTO DB mydb COLL mycoll ' 'WHEN MATCHED THEN KEEP;'
        ) == {
            '$merge': {
                'into': {'coll': 'mycoll', 'db': 'mydb'},
                'whenMatched': 'keepExisting',
            }
        }
        # MERGE
        assert Stages.parse(
            'MERGE INTO DB mydb COLL mycoll ' 'WHEN MATCHED THEN MERGE;'
        ) == {
            '$merge': {'into': {'coll': 'mycoll', 'db': 'mydb'}, 'whenMatched': 'merge'}
        }
        # FAIL
        assert Stages.parse(
            'MERGE INTO DB mydb COLL mycoll ' 'WHEN MATCHED THEN FAIL;'
        ) == {
            '$merge': {'into': {'coll': 'mycoll', 'db': 'mydb'}, 'whenMatched': 'fail'}
        }

        # with WHEN NOT MATCHED clause
        # INSERT
        assert Stages.parse(
            'MERGE INTO DB mydb COLL mycoll ' 'WHEN NOT MATCHED THEN INSERT;'
        ) == {
            '$merge': {
                'into': {'coll': 'mycoll', 'db': 'mydb'},
                'whenNotMatched': 'insert',
            }
        }
        # FAIL
        assert Stages.parse(
            'MERGE INTO DB mydb COLL mycoll ' 'WHEN NOT MATCHED THEN DISCARD;'
        ) == {
            '$merge': {
                'into': {'coll': 'mycoll', 'db': 'mydb'},
                'whenNotMatched': 'discard',
            }
        }
        # FAIL
        assert Stages.parse(
            'MERGE INTO DB mydb COLL mycoll ' 'WHEN NOT MATCHED THEN FAIL;'
        ) == {
            '$merge': {
                'into': {'coll': 'mycoll', 'db': 'mydb'},
                'whenNotMatched': 'fail',
            }
        }

        # overall check
        # empty pipeline
        with raises(ParseException):
            Stages.parse(
                '''
                MERGE INTO DB voting COLL monthlytotals
                ON _id
                WHEN MATCHED THEN
                    ()
                WHEN NOT MATCHED THEN
                    INSERT
                ;
                '''
            )
        # one pipeline
        assert (
            Stages.parse(
                '''
        MERGE INTO DB voting COLL monthlytotals
        ON _id
        WHEN MATCHED THEN
            (
                ADD FIELDS thumbsup + '$new.thumbsup' AS thumbsup,
                           thumbsdown + '$new.thumbsdown' AS thumbsdown;
            )
        WHEN NOT MATCHED THEN
            INSERT
        ;
        '''
            )
            == {
                '$merge': {
                    'into': {'db': 'voting', 'coll': 'monthlytotals'},
                    'on': ['_id'],
                    'whenMatched': [
                        {
                            '$addFields': {
                                'thumbsup': {'$add': ['$thumbsup', '$$new.thumbsup']},
                                'thumbsdown': {
                                    '$add': ['$thumbsdown', '$$new.thumbsdown']
                                },
                            }
                        }
                    ],
                    'whenNotMatched': "insert",
                }
            }
        )
        # two ONs, two pipelines
        assert (
            Stages.parse(
                '''
                MERGE INTO DB voting COLL monthlytotals
                ON _id, month
                WHEN MATCHED THEN
                    (
                        ADD FIELDS thumbsup + '$new.thumbsup' AS thumbsup,
                                   thumbsdown + '$new.thumbsdown' AS thumbsdown;
                        SET thumbsup + '$new.thumbsup' AS thumbsup,
                                   thumbsdown + '$new.thumbsdown' AS thumbsdown;
                    )
                WHEN NOT MATCHED THEN
                    INSERT
                ;
                '''
            )
            == {
                '$merge': {
                    'into': {'db': 'voting', 'coll': 'monthlytotals'},
                    'on': ['_id', 'month'],
                    'whenMatched': [
                        {
                            '$addFields': {
                                'thumbsup': {'$add': ['$thumbsup', '$$new.thumbsup']},
                                'thumbsdown': {
                                    '$add': ['$thumbsdown', '$$new.thumbsdown']
                                },
                            }
                        },
                        {
                            '$set': {
                                'thumbsup': {'$add': ['$thumbsup', '$$new.thumbsup']},
                                'thumbsdown': {
                                    '$add': ['$thumbsdown', '$$new.thumbsdown']
                                },
                            }
                        },
                    ],
                    'whenNotMatched': "insert",
                }
            }
        )
