from pyparsing import ParseException
from pytest import raises

from easymql.expressions import Expression


class TestBooleanExpression:
    @classmethod
    def setup_class(cls):
        cls.exp = Expression

    def test_and(self):
        assert self.exp.parse('AND(1, true, 3)') == {'$and': [1, True, 3]}
        with raises(ParseException):
            self.exp.parse('AND(1)')

    def test_not(self):
        assert self.exp.parse('NOT(1)') == {'$not': [1]}
        with raises(ParseException):
            self.exp.parse('NOT(1, true, 3)')

    def test_or(self):
        assert self.exp.parse('OR(1, true, 3)') == {'$or': [1, True, 3]}
        with raises(ParseException):
            self.exp.parse('OR(1)')
