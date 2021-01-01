from pyparsing import ParseException
from pytest import raises

from easymql.expressions import Expression


class TestArithmeticExpression:
    @classmethod
    def setup_class(cls):
        cls.exp = Expression()

    def test_abs(self):
        assert self.exp.parse('ABS(1)') == [{'$abs': [1]}]
        assert self.exp.parse('ABS([1])') == [{'$abs': [[1]]}]
        with raises(ParseException):
            self.exp.parse('ABS(1, 2)')

    def test_add(self):
        assert self.exp.parse('ADD(1, 2)') == [{'$add': [1, 2]}]
        assert self.exp.parse('ADD(1, 2, 3)') == [{'$add': [1, 2, 3]}]
        with raises(ParseException):
            self.exp.parse('ADD(1)')

    def test_ceil(self):
        assert self.exp.parse('CEIL(1)') == [{'$ceil': [1]}]
        with raises(ParseException):
            self.exp.parse('CEIL(1, 2)')

    def test_divide(self):
        assert self.exp.parse('DIVIDE(1, 2)') == [{'$divide': [1, 2]}]
        with raises(ParseException):
            self.exp.parse('DIVIDE(1, 2, 3)')
        with raises(ParseException):
            self.exp.parse('DIVIDE(1)')

    def test_exp(self):
        assert self.exp.parse('EXP(1)') == [{'$exp': [1]}]
        with raises(ParseException):
            self.exp.parse('EXP(1, 2)')

    def test_floor(self):
        assert self.exp.parse('FLOOR(1)') == [{'$floor': [1]}]
        with raises(ParseException):
            self.exp.parse('FLOOR(1, 2)')

    def test_ln(self):
        assert self.exp.parse('LN(1)') == [{'$ln': [1]}]
        with raises(ParseException):
            self.exp.parse('LN(1, 2)')

    def test_log(self):
        assert self.exp.parse('LOG(1, 2)') == [{'$log': [1, 2]}]
        with raises(ParseException):
            self.exp.parse('LOG(1, 2, 3)')
        with raises(ParseException):
            self.exp.parse('LOG(1)')

    def test_log10(self):
        assert self.exp.parse('LOG10(1)') == [{'$log10': [1]}]
        with raises(ParseException):
            self.exp.parse('LOG10(1, 2)')

    def test_mod(self):
        assert self.exp.parse('MOD(1, 2)') == [{'$mod': [1, 2]}]
        with raises(ParseException):
            self.exp.parse('MOD(1, 2, 3)')
        with raises(ParseException):
            self.exp.parse('MOD(1)')

    def test_multiply(self):
        assert self.exp.parse('MULTIPLY(1, 2)') == [{'$multiply': [1, 2]}]
        assert self.exp.parse('MULTIPLY(1, 2, 3)') == [{'$multiply': [1, 2, 3]}]
        with raises(ParseException):
            self.exp.parse('MULTIPLY(1)')

    def test_pow(self):
        assert self.exp.parse('POW(1, 2)') == [{'$pow': [1, 2]}]
        with raises(ParseException):
            self.exp.parse('POW(1, 2, 3)')
        with raises(ParseException):
            self.exp.parse('POW(1)')

    def test_round(self):
        assert self.exp.parse('ROUND(1)') == [{'$round': [1]}]
        assert self.exp.parse('ROUND(1, 2)') == [{'$round': [1, 2]}]
        with raises(ParseException):
            self.exp.parse('ROUND(1, 2, 3)')

    def test_sqrt(self):
        assert self.exp.parse('SQRT(1)') == [{'$sqrt': [1]}]
        with raises(ParseException):
            self.exp.parse('SQRT(1, 2)')

    def test_subtract(self):
        assert self.exp.parse('SUBTRACT(1, 2)') == [{'$subtract': [1, 2]}]
        with raises(ParseException):
            self.exp.parse('SUBTRACT(1, 2, 3)')
        with raises(ParseException):
            self.exp.parse('SUBTRACT(1)')

    def test_trunc(self):
        assert self.exp.parse('TRUNC(1)') == [{'$trunc': [1]}]
        assert self.exp.parse('TRUNC(1, 2)') == [{'$trunc': [1, 2]}]
        with raises(ParseException):
            self.exp.parse('TRUNC(1, 2, 3)')
