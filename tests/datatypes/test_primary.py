import pyparsing
import pytest

from easymql.datatypes.primary import (
    Boolean,
    BooleanFalse,
    BooleanTrue,
    Decimal,
    Integer,
    Null,
    Number,
    String,
)


class TestPrimaryDataType:
    def test_null(self):
        null = Null()
        assert null.parse('null') == [None]
        for value in ['None', 'NULL', '', '"null"', "'null'"]:
            with pytest.raises(pyparsing.ParseException):
                null.parse(value)

    def test_string(self):
        string = String()
        assert string.parse('"hello"') == ['hello']
        assert string.parse('"newline\ntest"') == ['newline\ntest']
        assert string.parse('"hello \\"world\\""') == ['hello "world"']
        assert string.parse("\"hello 'world'\"") == ["hello 'world'"]
        assert string.parse('"unicode \u1F600 test"') == ['unicode \u1F600 test']
        assert (
            string.parse(
                '''"multi
line"'''
            )
            == ['multi\nline']
        )
        with pytest.raises(pyparsing.ParseException):
            assert string.parse("'hello'") == ['hello']

    def test_boolean(self):
        true, false, boolean = BooleanTrue(), BooleanFalse(), Boolean()
        assert true.parse('true') == [True]
        assert false.parse('false') == [False]
        assert boolean.parse('true') == [True]
        assert boolean.parse('false') == [False]
        for value in ['TRUE', 1, '', True]:
            with pytest.raises((pyparsing.ParseException, AttributeError)):
                true.parse(value)
        for value in ['FALSE', 0, '', False]:
            with pytest.raises((pyparsing.ParseException, AttributeError)):
                false.parse(value)

    def test_integer(self):
        integer = Integer()
        assert integer.parse('123') == [123]
        assert integer.parse('+123') == [123]
        assert integer.parse('-123') == [-123]
        for value in ['123.1', '+123.1', '-123.1']:
            with pytest.raises(pyparsing.ParseException):
                integer.parse(value)

    def test_decimal(self):
        decimal = Decimal()
        assert decimal.parse('123.1') == [123.1]
        assert decimal.parse('+123.1') == [123.1]
        assert decimal.parse('-123.1') == [-123.1]
        assert decimal.parse('-123.1e1') == [-1231]
        assert decimal.parse('123.1E1') == [1231]

    def test_number(self):
        number = Number()
        assert number.parse('123') == [123]
        assert number.parse('+123') == [123]
        assert number.parse('-123') == [-123]
        assert number.parse('123.4') == [123.4]
        assert number.parse('-.123') == [-0.123]
        assert number.parse('+0.123') == [0.123]
        assert number.parse('-123.1e1') == [-1231]
        assert number.parse('123.1E1') == [1231]
