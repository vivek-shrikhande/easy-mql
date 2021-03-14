from easymql.core import Keyword

from easymql import Grammar
from easymql.actions import ExpressionAction
from easymql.basics import LPAREN, RPAREN
from easymql.proxies import expression_proxy


class BinarySize(Grammar, ExpressionAction):
    grammar = Keyword("BINARY_SIZE") + LPAREN + expression_proxy + RPAREN


class BsonSize(Grammar, ExpressionAction):
    grammar = Keyword("BSON_SIZE") + LPAREN + expression_proxy + RPAREN


class DataSizeExpression(Grammar):

    grammar = BinarySize | BsonSize
