from pyparsing import ParseException
from pytest import raises

from easymql.expressions import Expression


class TestTrigonometryExpression:
    @classmethod
    def setup_class(cls):
        cls.exp = Expression

    def test_sin(self):
        assert self.exp.parse('SIN(1.2)') == {'$sin': [1.2]}
        with raises(ParseException):
            self.exp.parse('SIN()')

    def test_cos(self):
        assert self.exp.parse('COS(1.2)') == {'$cos': [1.2]}
        with raises(ParseException):
            self.exp.parse('COS()')

    def test_tan(self):
        assert self.exp.parse('TAN(1.2)') == {'$tan': [1.2]}
        with raises(ParseException):
            self.exp.parse('TAN()')

    def test_asin(self):
        assert self.exp.parse('ASIN(1.2)') == {'$asin': [1.2]}
        with raises(ParseException):
            self.exp.parse('ASIN()')

    def test_acos(self):
        assert self.exp.parse('ACOS(1.2)') == {'$acos': [1.2]}
        with raises(ParseException):
            self.exp.parse('ACOS()')

    def test_atan(self):
        assert self.exp.parse('ATAN(1.2)') == {'$atan': [1.2]}
        with raises(ParseException):
            self.exp.parse('ATAN()')

    def test_atan2(self):
        assert self.exp.parse('ATAN2(1.2, 2.5)') == {'$atan2': [1.2, 2.5]}
        with raises(ParseException):
            self.exp.parse('ATAN2()')

    def test_asinh(self):
        assert self.exp.parse('ASINH(1.2)') == {'$asinh': [1.2]}
        with raises(ParseException):
            self.exp.parse('ASINH()')

    def test_acosh(self):
        assert self.exp.parse('ACOSH(1.2)') == {'$acosh': [1.2]}
        with raises(ParseException):
            self.exp.parse('ACOSH()')

    def test_atanh(self):
        assert self.exp.parse('ATANH(1.2)') == {'$atanh': [1.2]}
        with raises(ParseException):
            self.exp.parse('ATANH()')

    def test_degrees_to_radians(self):
        assert self.exp.parse('DEGREES_TO_RADIANS(1.2)') == {'$degreesToRadians': [1.2]}

        with raises(ParseException):
            self.exp.parse('DEGREES_TO_RADIANS()')

    def test_radians_to_degrees(self):
        assert self.exp.parse('RADIANS_TO_DEGREES(1.2)') == {'$radiansToDegrees': [1.2]}

        with raises(ParseException):
            self.exp.parse('RADIANS_TO_DEGREES()')
