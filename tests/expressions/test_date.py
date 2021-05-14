from pyparsing import ParseException
from pytest import raises

from easymql.datatypes.primary import Date
from easymql.datatypes.primary import Integer
from easymql.expressions import FuncExpression


class TestDateExpression:
    @classmethod
    def setup_class(cls):
        cls.exp = FuncExpression

    def test_date(self):
        with raises(ParseException):
            self.exp.parse('DATE()')
        assert self.exp.parse('DATE(2000)') == {
            '$dateFromParts': {'year': Integer(2000)}
        }
        assert self.exp.parse('DATE(2000, 11)') == {
            '$dateFromParts': {'year': Integer(2000), 'month': Integer(11)}
        }
        assert self.exp.parse('DATE(2000, 11, 1 + 3)') == {
            '$dateFromParts': {
                'year': Integer(2000),
                'month': Integer(11),
                'day': {'$add': [Integer(1), Integer(3)]},
            }
        }
        assert self.exp.parse('DATE(2000, 11, 24, 12)') == {
            '$dateFromParts': {
                'year': Integer(2000),
                'month': Integer(11),
                'day': Integer(24),
                'hour': Integer(12),
            }
        }
        assert self.exp.parse('DATE(2000, 11, 24, 12, 30)') == {
            '$dateFromParts': {
                'year': 2000,
                'month': 11,
                'day': 24,
                'hour': 12,
                'minute': 30,
            }
        }
        assert self.exp.parse('DATE(2000, 11, 24, 12, 30, 56)') == {
            '$dateFromParts': {
                'year': 2000,
                'month': 11,
                'day': 24,
                'hour': 12,
                'minute': 30,
                'second': 56,
            }
        }
        assert self.exp.parse('DATE(2000, 11, 24, 12, 30, 56, 456)') == {
            '$dateFromParts': {
                'year': 2000,
                'month': 11,
                'day': 24,
                'hour': 12,
                'minute': 30,
                'second': 56,
                'millisecond': 456,
            }
        }
        assert self.exp.parse('DATE(2000, 11, 24, 12, 30, 56, 456, "+0530")') == {
            '$dateFromParts': {
                'year': 2000,
                'month': 11,
                'day': 24,
                'hour': 12,
                'minute': 30,
                'second': 56,
                'millisecond': 456,
                'timezone': '+0530',
            }
        }

    def test_iso_week_date(self):
        with raises(ParseException):
            self.exp.parse('ISO_WEEK_DATE()')
        assert self.exp.parse('ISO_WEEK_DATE(2000)') == {
            '$dateFromParts': {'isoWeekYear': Integer(2000)}
        }
        assert self.exp.parse('ISO_WEEK_DATE(2000, 11)') == {
            '$dateFromParts': {'isoWeekYear': Integer(2000), 'isoWeek': Integer(11)}
        }
        assert self.exp.parse('ISO_WEEK_DATE(2000, 11, 1 + 3)') == {
            '$dateFromParts': {
                'isoWeekYear': Integer(2000),
                'isoWeek': Integer(11),
                'isoDayOfWeek': {'$add': [Integer(1), Integer(3)]},
            }
        }
        assert self.exp.parse('ISO_WEEK_DATE(2000, 11, 5, 12)') == {
            '$dateFromParts': {
                'isoWeekYear': Integer(2000),
                'isoWeek': Integer(11),
                'isoDayOfWeek': Integer(5),
                'hour': Integer(12),
            }
        }
        assert self.exp.parse('ISO_WEEK_DATE(2000, 11, 5, 12, 30)') == {
            '$dateFromParts': {
                'isoWeekYear': 2000,
                'isoWeek': 11,
                'isoDayOfWeek': 5,
                'hour': 12,
                'minute': 30,
            }
        }
        assert self.exp.parse('ISO_WEEK_DATE(2000, 11, 5, 12, 30, 56)') == {
            '$dateFromParts': {
                'isoWeekYear': 2000,
                'isoWeek': 11,
                'isoDayOfWeek': 5,
                'hour': 12,
                'minute': 30,
                'second': 56,
            }
        }
        assert self.exp.parse('ISO_WEEK_DATE(2000, 11, 6, 12, 30, 56, 456)') == {
            '$dateFromParts': {
                'isoWeekYear': 2000,
                'isoWeek': 11,
                'isoDayOfWeek': 6,
                'hour': 12,
                'minute': 30,
                'second': 56,
                'millisecond': 456,
            }
        }
        assert self.exp.parse(
            'ISO_WEEK_DATE(2000, 11, 6, 12, 30, 56, 456, "+0530")'
        ) == {
            '$dateFromParts': {
                'isoWeekYear': 2000,
                'isoWeek': 11,
                'isoDayOfWeek': 6,
                'hour': 12,
                'minute': 30,
                'second': 56,
                'millisecond': 456,
                'timezone': '+0530',
            }
        }

    def test_parse_date(self):
        with raises(ParseException):
            self.exp.parse('PARSE_DATE()')
        assert self.exp.parse('PARSE_DATE("2020-01-15T12:30:59.932-12:00")') == {
            '$dateFromString': {'dateString': '2020-01-15T12:30:59.932-12:00'}
        }
        assert self.exp.parse('PARSE_DATE("06-15-2018", "%m-%d-%Y")') == {
            '$dateFromString': {'dateString': '06-15-2018', 'format': '%m-%d-%Y'}
        }
        # Result should not contain 'format' in it is 'null'
        assert self.exp.parse(
            'PARSE_DATE("2017-02-08T12:10:40.787", null, "America/New_York")'
        ) == {
            '$dateFromString': {
                'dateString': '2017-02-08T12:10:40.787',
                'timezone': 'America/New_York',
            }
        }
        assert self.exp.parse(
            'PARSE_DATE("2017-02-08T12:10:40.787Z", "%Y-%m-%dT%H:%M:%S.%LZ", "America/New_York")'
        ) == {
            '$dateFromString': {
                'dateString': '2017-02-08T12:10:40.787Z',
                'format': '%Y-%m-%dT%H:%M:%S.%LZ',
                'timezone': 'America/New_York',
            }
        }

    def test_format_date(self):
        with raises(ParseException):
            self.exp.parse('FORMAT_DATE()')
        assert self.exp.parse('FORMAT_DATE(D"2020-01-15T12:30:59.932-12:00")') == {
            '$dateToString': {'date': Date(2020, 1, 15, 12, 30, 59, 932, '-12:00')}
        }
        assert self.exp.parse(
            'FORMAT_DATE(D"2020-01-15T12:30:59.932-12:00", "%m-%d-%Y")'
        ) == {
            '$dateToString': {
                'date': Date(2020, 1, 15, 12, 30, 59, 932, '-12:00'),
                'format': '%m-%d-%Y',
            }
        }
        assert self.exp.parse(
            'FORMAT_DATE(D"2020-01-15T12:30:59.932-12:00", null, "America/New_York")'
        ) == {
            '$dateToString': {
                'date': Date(2020, 1, 15, 12, 30, 59, 932, '-12:00'),
                'timezone': 'America/New_York',
            }
        }
        assert self.exp.parse(
            'FORMAT_DATE(D"2020-01-15T12:30:59.932-12:00", "%Y-%m-%dT%H:%M:%S.%LZ", "America/New_York")'
        ) == {
            '$dateToString': {
                'date': Date(2020, 1, 15, 12, 30, 59, 932, '-12:00'),
                'format': '%Y-%m-%dT%H:%M:%S.%LZ',
                'timezone': 'America/New_York',
            }
        }

    def test_extract(self):
        assert self.exp.parse(
            'EXTRACT(MILLISECOND, D"2020-01-15T12:30:59.932-12:00")'
        ) == {'$millisecond': {'date': Date(2020, 1, 15, 12, 30, 59, 932, '-12:00')}}
        assert self.exp.parse('EXTRACT(SECOND, D"2020-01-15T12:30:59.932")') == {
            '$second': {'date': Date(2020, 1, 15, 12, 30, 59, 932)}
        }
        assert self.exp.parse('EXTRACT(MINUTE, D"2020-01-15T12:30:59")') == {
            '$minute': {'date': Date(2020, 1, 15, 12, 30, 59)}
        }
        assert self.exp.parse('EXTRACT(HOUR, D"2020-01-15T12:30:59.932")') == {
            '$hour': {'date': Date(2020, 1, 15, 12, 30, 59, 932)}
        }
        assert self.exp.parse('EXTRACT(DAY_OF_MONTH, D"2020-01-15")') == {
            '$day': {'date': Date(2020, 1, 15)}
        }
        assert self.exp.parse('EXTRACT(MONTH, D"2020-01")') == {
            '$month': {'date': Date(2020, 1)}
        }
        assert self.exp.parse('EXTRACT(YEAR, D"2020")') == {
            '$year': {'date': Date(2020)}
        }
        assert self.exp.parse('EXTRACT(DAY_OF_WEEK, D"2020-01-15T12:30:59.932Z")') == {
            '$dayOfWeek': {'date': Date(2020, 1, 15, 12, 30, 59, 932, 'Z')}
        }
        assert self.exp.parse('EXTRACT(ISO_DAY_OF_WEEK, D"2020-01-15T12:30:59Z")') == {
            '$isoDayOfWeek': {'date': Date(2020, 1, 15, 12, 30, 59)}
        }
        assert self.exp.parse('EXTRACT(DAY_OF_YEAR, D"2020-01-15")') == {
            '$dayOfYear': {'date': Date(2020, 1, 15)}
        }
        assert self.exp.parse('EXTRACT(WEEK, D"2020-01-15T12:30:59.932-12:00")') == {
            '$week': {'date': Date(2020, 1, 15, 12, 30, 59, 932, '-12:00')}
        }
        assert self.exp.parse(
            'EXTRACT(ISO_WEEK, D"2020-01-15T12:30:59.932-12:00")'
        ) == {'$isoWeek': {'date': Date(2020, 1, 15, 12, 30, 59, 932, '-12:00')}}
        assert self.exp.parse(
            'EXTRACT(ISO_YEAR, D"2020-01-15T12:30:59.932-12:00")'
        ) == {'$isoYear': {'date': Date(2020, 1, 15, 12, 30, 59, 932, '-12:00')}}
        with raises(ParseException):
            self.exp.parse('EXTRACT(HOU, D"2020-01-15")')
