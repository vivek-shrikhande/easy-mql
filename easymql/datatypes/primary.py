from pyparsing import Keyword, pyparsing_common, QuotedString, Regex

from easymql import Grammar
from easymql.basics import LPAREN, RPAREN


class Null(Grammar):

    grammar = Keyword('null')

    @staticmethod
    def action():
        return [None]


class String(Grammar):

    grammar = QuotedString(quoteChar='"', escChar='\\', multiline=True)

    @staticmethod
    def action(token):
        return token


class BooleanTrue(Grammar):

    grammar = Keyword('true')

    @staticmethod
    def action():
        return [True]


class BooleanFalse(Grammar):

    grammar = Keyword('false')

    @staticmethod
    def action():
        return [False]


class Boolean(Grammar):

    grammar = BooleanTrue() | BooleanFalse()


class Integer(Grammar):

    grammar = pyparsing_common.signed_integer

    @staticmethod
    def action(token):
        return int(token[0])


class Decimal(Grammar):

    grammar = pyparsing_common.sci_real | pyparsing_common.real


class Number(Grammar):

    grammar = pyparsing_common.number


class DatePart(Grammar):

    range_map = {
        'year': {'min': 0, 'max': 9999},
        'month': {'min': 1, 'max': 12},
        'day': {'min': 1, 'max': 31},
        'hour': {'min': 0, 'max': 23},
        'minute': {'min': 0, 'max': 59},
        'second': {'min': 0, 'max': 59},
        'millisecond': {'min': 0, 'max': 999},
        'tzhour': {'min': 0, 'max': 23},
        'tzminute': {'min': 0, 'max': 59},
    }

    def action(self, tokens):
        for k, v in tokens.items():
            try:
                self.check_range(k.title(), int(v), **self.range_map[k])
            except TypeError:
                pass

    def check_range(self, part, value, min, max):
        if value < min or value > max:
            raise ValueError(f'{part}({value}) is out of range [{min}-{max}]')


class Time(DatePart):

    grammar = Regex(
        r'(?P<hour>\d{2}):(?P<minute>\d{2})(:(?P<second>\d{2})(\.(?P<millisecond>\d{3}))?)?'
    )


class TimeZone(DatePart):

    grammar = Regex(r'(Z|[+-](?P<tzhour>\d{2})(:?(?P<tzminute>\d{2}))?)?')


class Date(DatePart):

    grammar = Regex(
        r'D"(?P<year>\d{4})(-(?P<month>\d{2})(-(?P<day>\d{2}))?)?'
        r'([T ](?P<hour>\d{2}):(?P<minute>\d{2})(:(?P<second>\d{2})(\.(?P<millisecond>\d{3}))?)?'
        r'(?P<timezone>(Z|[+-](?P<tzhour>\d{2})(:?(?P<tzminute>\d{2}))?))?)?"'
    )

    def action(self, tokens):
        timezone = tokens.pop('timezone')
        super().action(tokens)
        obj = {}
        for part in ['year', 'month', 'day', 'hour', 'minute', 'second', 'millisecond']:
            try:
                value = int(tokens[part])
            except (TypeError, ValueError):
                pass
            else:
                obj[part] = value
        if timezone is not None:
            obj['timezone'] = timezone
        return {'$dateFromParts': obj}
