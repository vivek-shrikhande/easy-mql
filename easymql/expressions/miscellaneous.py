from easymql.core import Keyword

from easymql import Grammar
from easymql.actions import ExpressionAction
from easymql.basics import LPAREN, RPAREN
from easymql.datatypes.primary import Decimal


class Random(Grammar, ExpressionAction):

    grammar = Keyword("RANDOM") + LPAREN + RPAREN

    @staticmethod
    def action(tokens):
        return {'$rand': {}}


class SampleRate(Grammar, ExpressionAction):

    grammar = Keyword("SAMPLE_RATE") + LPAREN + Decimal + RPAREN


class MiscellaneousExpression(Grammar):

    grammar = Random | SampleRate
