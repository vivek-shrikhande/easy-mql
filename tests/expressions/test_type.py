from pyparsing import ParseException
from pytest import raises

from easymql.expressions import Expression


class TestTypeExpression:
    @classmethod
    def setup_class(cls):
        cls.exp = Expression()

    def test_is_number(self):
        assert self.exp.parse('IS_NUMBER("grade")') == [{'$isNumber': ["grade"]}]
        with raises(ParseException):
            self.exp.parse('IS_NUMBER()')

    def test_to_bool(self):
        assert self.exp.parse('TO_BOOL("true")') == [{'$toBool': ["true"]}]
        with raises(ParseException):
            self.exp.parse('TO_BOOL()')

    def test_to_date(self):
        assert self.exp.parse('TO_DATE("2018-03-03")') == [{'$toDate': ["2018-03-03"]}]
        with raises(ParseException):
            self.exp.parse('TO_DATE()')

    def test_to_decimal(self):
        assert self.exp.parse('TO_DECIMAL(27)') == [{'$toDecimal': [27]}]
        with raises(ParseException):
            self.exp.parse('TO_DECIMAL()')

    def test_to_double(self):
        assert self.exp.parse('TO_DOUBLE(3)') == [{'$toDouble': [3]}]
        with raises(ParseException):
            self.exp.parse('TO_DOUBLE()')

    def test_to_int(self):
        assert self.exp.parse('TO_INT(2.5)') == [{'$toInt': [2.5]}]
        with raises(ParseException):
            self.exp.parse('TO_INT()')

    def test_to_long(self):
        assert self.exp.parse('TO_LONG(2.5)') == [{'$toLong': [2.5]}]
        with raises(ParseException):
            self.exp.parse('TO_LONG()')

    def test_to_object_id(self):
        assert self.exp.parse('TO_OBJECT_ID("5ab9cbfa31c2ab715d42129e")') == [
            {'$toObjectId': ["5ab9cbfa31c2ab715d42129e"]}
        ]
        with raises(ParseException):
            self.exp.parse('TO_OBJECT_ID()')

    def test_to_string(self):
        assert self.exp.parse('TO_STRING(2.5)') == [{'$toString': [2.5]}]
        with raises(ParseException):
            self.exp.parse('TO_STRING()')

    def test_type(self):
        assert self.exp.parse('TYPE(2.5)') == [{'$type': [2.5]}]
        with raises(ParseException):
            self.exp.parse('TYPE()')
