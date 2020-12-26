from pyparsing import Keyword, QuotedString
from pyparsing import pyparsing_common

from easymql import Grammar


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
