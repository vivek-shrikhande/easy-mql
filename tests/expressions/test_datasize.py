from pyparsing import ParseException
from pytest import raises

from easymql.expressions import Expression


class TestDataSizeOperator:
    @classmethod
    def setup_class(cls):
        cls.exp = Expression

    def test_binary_size(self):
        assert self.exp.parse('BINARY_SIZE("someString")') == {'$binarySize': ['someString']}

        with raises(ParseException):
            self.exp.parse('BINARY_SIZE()')

    def test_bson_size(self):
        assert self.exp.parse('BSON_SIZE({"a": 1, "b": 2})') == {'$bsonSize': [{"a": 1, "b": 2}]}

        with raises(ParseException):
            self.exp.parse('BSON_SIZE()')
