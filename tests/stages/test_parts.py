from pyparsing import ParseException
from pytest import raises

from easymql.stages.parts import CollectionName, Field, DbName, DbCollectionPath, Alias


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

    def test_db_collection_path(self):
        assert DbCollectionPath.parse('DB my_db COLL my_collection') == {
            'db': 'my_db',
            'coll': 'my_collection',
        }
        assert DbCollectionPath.parse('COLL my_collection') == 'my_collection'
        with raises(ParseException):
            DbCollectionPath.parse('DB my_db')

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

    def test_alias(self):
        assert Alias.parse('1 + 2 AS sum') == {'sum': {'$add': [1, 2]}}
        assert Alias.parse('"hello world" AS greeting') == {'greeting': "hello world"}
        with raises(ParseException):
            Alias.parse('sum AS 1 + 2')
