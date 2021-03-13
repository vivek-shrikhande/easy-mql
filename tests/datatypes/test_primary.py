import pytest
from pyparsing import ParseException

from easymql.datatypes.primary import (
    Boolean,
    Date,
    Decimal,
    Integer,
    Null,
    Number,
    String,
)
from easymql.exc import DatePartOutOfRangeError


class TestPrimaryDataType:
    def test_null(self):
        assert Null.parse('null') == Null(None)
        for value in ['None', 'NULL', '', '"null"', "'null'"]:
            with pytest.raises(ParseException):
                Null.parse(value)

    def test_string(self):
        assert String.parse('"hello"') == String('hello')
        assert String.parse('"newline\ntest"') == String('newline\ntest')
        assert String.parse('"hello \\"world\\""') == String('hello "world"')
        assert String.parse("\"hello 'world'\"") == String("hello 'world'")
        assert String.parse('"unicode \u1F600 test"') == String('unicode \u1F600 test')
        assert (
            String.parse(
                '''"multi
line"'''
            )
            == String('multi\nline')
        )
        with pytest.raises(ParseException):
            assert String.parse("'hello'") == String('hello')

    def test_boolean(self):
        assert Boolean.parse('true') == Boolean(True)
        assert Boolean.parse('false') == Boolean(False)
        assert Boolean.parse('true') == Boolean(True)
        assert Boolean.parse('false') == Boolean(False)
        for value in ['TRUE', 1, '', True]:
            with pytest.raises((ParseException, AttributeError)):
                Boolean.parse(value)
        for value in ['FALSE', 0, '', False]:
            with pytest.raises((ParseException, AttributeError)):
                Boolean.parse(value)

    def test_integer(self):
        assert Integer.parse('123') == Integer(123)
        assert Integer.parse('+123') == Integer(123)
        assert Integer.parse('-123') == Integer(-123)
        for value in ['123.1', '+123.1', '-123.1']:
            with pytest.raises(ParseException):
                Integer.parse(value)

    def test_decimal(self):
        assert Decimal.parse('123.1') == Decimal(123.1)
        assert Decimal.parse('+123.1') == Decimal(123.1)
        assert Decimal.parse('-123.1') == Decimal(-123.1)
        assert Decimal.parse('-123.1e1') == Decimal(-1231)
        assert Decimal.parse('123.1E1') == Decimal(1231)

    def test_number(self):
        assert Number.parse('123') == Integer(123)
        assert Number.parse('+123') == Integer(123)
        assert Number.parse('-123') == Integer(-123)
        assert Number.parse('123.4') == Decimal(123.4)
        assert Number.parse('-.123') == Decimal(-0.123)
        assert Number.parse('+0.123') == Decimal(0.123)
        assert Number.parse('-123.1e1') == Decimal(-1231)
        assert Number.parse('123.1E1') == Decimal(1231)

    def test_date(self):
        date = Date.parse('D"2021"')
        assert date == Date(2021)
        assert date.value == {
            '$dateFromParts': {
                'year': 2021,
                'month': 1,
                'day': 1,
                'hour': 0,
                'minute': 0,
                'second': 0,
                'millisecond': 0,
                'timezone': 'Z',
            }
        }

        date = Date.parse('D"2021-01"')
        assert date == Date(2021, 1)
        assert date.value == {
            '$dateFromParts': {
                'year': 2021,
                'month': 1,
                'day': 1,
                'hour': 0,
                'minute': 0,
                'second': 0,
                'millisecond': 0,
                'timezone': 'Z',
            }
        }

        date = Date.parse('D"2021-01-01"')
        assert date == Date(2021, 1, 1)
        assert date.value == {
            '$dateFromParts': {
                'year': 2021,
                'month': 1,
                'day': 1,
                'hour': 0,
                'minute': 0,
                'second': 0,
                'millisecond': 0,
                'timezone': 'Z',
            }
        }

        date = Date.parse('D"2021-01-01T12:14"')
        assert date == Date(2021, 1, 1, 12, 14)
        assert date.value == {
            '$dateFromParts': {
                'year': 2021,
                'month': 1,
                'day': 1,
                'hour': 12,
                'minute': 14,
                'second': 0,
                'millisecond': 0,
                'timezone': 'Z',
            }
        }

        date = Date.parse('D"2021-01-01 12:14"')
        assert date == Date(2021, 1, 1, 12, 14)
        assert date.value == {
            '$dateFromParts': {
                'year': 2021,
                'month': 1,
                'day': 1,
                'hour': 12,
                'minute': 14,
                'second': 0,
                'millisecond': 0,
                'timezone': 'Z',
            }
        }

        date = Date.parse('D"2021-01-01T12:14:00"')
        assert date == Date(2021, 1, 1, 12, 14, 0)
        assert date.value == {
            '$dateFromParts': {
                'year': 2021,
                'month': 1,
                'day': 1,
                'hour': 12,
                'minute': 14,
                'second': 0,
                'millisecond': 0,
                'timezone': 'Z',
            }
        }

        date = Date.parse('D"2021-01-01T12:14:00Z"')
        assert date == Date(2021, 1, 1, 12, 14, 0)
        assert date.value == {
            '$dateFromParts': {
                'year': 2021,
                'month': 1,
                'day': 1,
                'hour': 12,
                'minute': 14,
                'second': 0,
                'millisecond': 0,
                'timezone': 'Z',
            }
        }

        date = Date.parse('D"2021-01-01T12:14:00-05"')
        assert date == Date(2021, 1, 1, 12, 14, 0, timezone='-05')
        assert date.value == {
            '$dateFromParts': {
                'year': 2021,
                'month': 1,
                'day': 1,
                'hour': 12,
                'minute': 14,
                'second': 0,
                'millisecond': 0,
                'timezone': '-05',
            }
        }

        date = Date.parse('D"2021-01-01T12:14:00+05:30"')
        assert date == Date(2021, 1, 1, 12, 14, 0, timezone='+05:30')
        assert date.value == {
            '$dateFromParts': {
                'year': 2021,
                'month': 1,
                'day': 1,
                'hour': 12,
                'minute': 14,
                'second': 0,
                'millisecond': 0,
                'timezone': '+05:30',
            }
        }

        date = Date.parse('D"2021-01-01T12:14:00+0530"')
        assert date == Date(2021, 1, 1, 12, 14, 0, timezone='+0530')
        assert date.value == {
            '$dateFromParts': {
                'year': 2021,
                'month': 1,
                'day': 1,
                'hour': 12,
                'minute': 14,
                'second': 0,
                'millisecond': 0,
                'timezone': '+0530',
            }
        }

        date = Date.parse('D"2021-01-15T12:30:59.932-12:00"')
        assert date == Date(2021, 1, 15, 12, 30, 59, 932, '-12:00')
        assert date.value == {
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

        # space between D and date string
        with pytest.raises(ParseException):
            Date.parse('D "2021-01-01 12:14:00+0530"')

        # double space
        with pytest.raises(ParseException):
            Date.parse('D"2021-01-012021-01-01T12:14:00-05  12:14:00+0530"')

        # whitespaces
        with pytest.raises(ParseException):
            Date.parse('D"2021 - 01 - 01T12 : 14 : 00 + 0530"')

        # year out of range
        for year in [-1, 10000]:
            with pytest.raises((ParseException, DatePartOutOfRangeError)):
                Date.parse(f'D"{year}"')

        # month out of range
        for month in [0, 13]:
            with pytest.raises((ParseException, DatePartOutOfRangeError)):
                Date.parse(f'D"1970-{month}"')

        # day out of range
        for day in [0, 32]:
            with pytest.raises((ParseException, DatePartOutOfRangeError)):
                Date.parse(f'D"2000-12-{day}"')

        # hour out of range
        for hour in [-1, 24]:
            with pytest.raises((ParseException, DatePartOutOfRangeError)):
                Date.parse(f'D"2021-01-15 {hour}:30"')

        # minute out of range
        for minute in [-1, 60]:
            with pytest.raises((ParseException, DatePartOutOfRangeError)):
                Date.parse(f'D"2021-01-15T12:{minute}"')

        # second out of range
        for second in [-1, 60]:
            with pytest.raises((ParseException, DatePartOutOfRangeError)):
                Date.parse(f'D"2021-01-15 12:30:{second}"')

        # millisecond out of range
        for millisecond in [-1, 1000]:
            with pytest.raises((ParseException, DatePartOutOfRangeError)):
                Date.parse(f'D"2021-01-15T12:30:59.{millisecond}"')

        # tzhour out of range
        for tzhour in [-27, 27]:
            with pytest.raises((ParseException, DatePartOutOfRangeError)):
                Date.parse(f'D"2021-01-15T12:30:59.932+{tzhour}:30"')

        # tzminute out of range
        for tzminute in [-1, 60]:
            with pytest.raises((ParseException, DatePartOutOfRangeError)):
                Date.parse(f'D"2021-01-15T12:30:59.932-12:{tzminute}"')
