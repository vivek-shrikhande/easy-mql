from pyparsing import ParseException
from pytest import raises

from easymql.expressions import Expression as exp


class TestComparisonExpression:
    def test_cmp(self):
        assert exp.parse('CMP(1, 2)') == {'$cmp': [1, 2]}
        with raises(ParseException):
            exp.parse('CMP(1)')
        with raises(ParseException):
            exp.parse('CMP(1, 2, 3)')
        assert exp.parse('CMP(1, 3 + 2)') == {'$cmp': [1, {'$add': [3, 2]}]}
