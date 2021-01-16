import pyparsing
import pytest

from easymql.datatypes.primary import (
    Boolean,
    BooleanFalse,
    BooleanTrue,
    Date,
    DateTime,
    Decimal,
    Integer,
    Null,
    Number,
    String,
    Time,
    TimeZone,
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

    def test_date(self):
        date = Date()
        assert date.parse('2020') == ['2020']  # only year
        assert date.parse('2020-11') == ['2020-11']  # year, month
        assert date.parse('2020-11-01') == ['2020-11-01']  # year, month, day
        # year out of range
        for year in [-1, 10000]:
            with pytest.raises((pyparsing.ParseException, ValueError)):
                date.parse(f'{year}')
        # month out of range
        for month in [0, 13]:
            with pytest.raises((pyparsing.ParseException, ValueError)):
                date.parse(f'1970-{month}')
        # day out of range
        for day in [0, 32]:
            with pytest.raises((pyparsing.ParseException, ValueError)):
                date.parse(f'2000-12-{day}')

    def test_time(self):
        time = Time()
        with pytest.raises(pyparsing.ParseException):
            assert time.parse('12') == ['12']  # only hour
        assert time.parse('12:30') == ['12:30']
        # hour out of range
        for hour in [-1, 24]:
            with pytest.raises((pyparsing.ParseException, ValueError)):
                time.parse(f'{hour}:30')
        # minute out of range
        for minute in [-1, 60]:
            with pytest.raises((pyparsing.ParseException, ValueError)):
                time.parse(f'12:{minute}')
        assert time.parse('12:30:00') == ['12:30:00']
        # second out of range
        for second in [-1, 60]:
            with pytest.raises((pyparsing.ParseException, ValueError)):
                time.parse(f'12:30:{second}')
        assert time.parse('12:30:59.234') == ['12:30:59.234']
        # millisecond out of range
        for millisecond in [-1, 1000]:
            with pytest.raises((pyparsing.ParseException, ValueError)):
                time.parse(f'12:30:59.{millisecond}')

    def test_timezone(self):
        timezone = TimeZone()
        assert timezone.parse('') == ['']
        assert timezone.parse('Z') == ['Z']
        with pytest.raises(pyparsing.ParseException):
            timezone.parse('z')  # small 'z'
        assert timezone.parse('+08') == ['+08']
        assert timezone.parse('+08:00') == ['+08:00']
        assert timezone.parse('-0830') == ['-0830']
        # hour out of range
        for hour in [-1, 24]:
            with pytest.raises((pyparsing.ParseException, ValueError)):
                timezone.parse(f'+{hour}:30')
        # minute out of range
        for minute in [-1, 60]:
            with pytest.raises((pyparsing.ParseException, ValueError)):
                timezone.parse(f'-12:{minute}')

    def test_datetime(self):
        datetime = DateTime()
        assert datetime.parse('2021') == ['2021']
        assert datetime.parse('2021-01') == ['2021-01']
        assert datetime.parse('2021-01-01') == ['2021-01-01']
        assert datetime.parse('2021-01-01T12:14') == ['2021-01-01T12:14']
        assert datetime.parse('2021-01-01 12:14') == ['2021-01-01 12:14']
        assert datetime.parse('2021-01-01T12:14:00') == ['2021-01-01T12:14:00']
        assert datetime.parse('2021-01-01T12:14:00Z') == ['2021-01-01T12:14:00Z']
        assert datetime.parse('2021-01-01T12:14:00-05') == ['2021-01-01T12:14:00-05']
        assert datetime.parse('2021-01-01T12:14:00+05:30') == [
            '2021-01-01T12:14:00+05:30'
        ]
        assert datetime.parse('2021-01-01T12:14:00+0530') == [
            '2021-01-01T12:14:00+0530'
        ]
        # double space
        with pytest.raises(pyparsing.ParseException):
            datetime.parse('2021-01-01  12:14:00+0530')
        # whitespaces
        with pytest.raises(pyparsing.ParseException):
            datetime.parse('2021 - 01 - 01T12 : 14 : 00 + 0530')
        # year out of range
        for year in [-1, 10000]:
            with pytest.raises((pyparsing.ParseException, ValueError)):
                datetime.parse(f'{year}')
        # month out of range
        for month in [0, 13]:
            with pytest.raises((pyparsing.ParseException, ValueError)):
                datetime.parse(f'1970-{month}')
        # day out of range
        for day in [0, 32]:
            with pytest.raises((pyparsing.ParseException, ValueError)):
                datetime.parse(f'2000-12-{day}')
        # hour out of range
        for hour in [-1, 24]:
            with pytest.raises((pyparsing.ParseException, ValueError)):
                datetime.parse(f'2021-01-15 {hour}:30')
        # minute out of range
        for minute in [-1, 60]:
            with pytest.raises((pyparsing.ParseException, ValueError)):
                datetime.parse(f'2021-01-15T12:{minute}')
        # second out of range
        for second in [-1, 60]:
            with pytest.raises((pyparsing.ParseException, ValueError)):
                datetime.parse(f'2021-01-15 12:30:{second}')
        # millisecond out of range
        for millisecond in [-1, 1000]:
            with pytest.raises((pyparsing.ParseException, ValueError)):
                datetime.parse(f'2021-01-15T12:30:59.{millisecond}')
        # hour out of range
        for hour in [-1, 24]:
            with pytest.raises((pyparsing.ParseException, ValueError)):
                datetime.parse(f'2021-01-15T12:30:59.932+{hour}:30')
        # minute out of range
        for minute in [-1, 60]:
            with pytest.raises((pyparsing.ParseException, ValueError)):
                datetime.parse(f'2021-01-15T12:30:59.932-12:{minute}')
