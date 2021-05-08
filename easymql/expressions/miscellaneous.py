from easymql import Grammar
from easymql.actions import ExpressionAction, UnaryExpressionAction
from easymql.basics import LPAREN, RPAREN
from easymql.datatypes.primary import Decimal
from easymql.keywords import RANDOM, SAMPLE_RATE


class Random(Grammar, ExpressionAction):

    grammar = RANDOM + LPAREN + RPAREN

    @staticmethod
    def action(tokens):
        return {'$rand': {}}


class SampleRate(Grammar, UnaryExpressionAction):

    grammar = SAMPLE_RATE + LPAREN + Decimal + RPAREN


MiscellaneousExpression = Random | SampleRate
