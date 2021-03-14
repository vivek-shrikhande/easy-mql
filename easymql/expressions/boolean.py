from easymql.core import Keyword

from easymql import Grammar
from easymql.actions import ExpressionAction
from easymql.basics import LPAREN, RPAREN
from easymql.proxies import expression_proxy
from easymql.utils import delimited_list


class And(Grammar, ExpressionAction):

    grammar = Keyword("AND") + LPAREN + delimited_list(expression_proxy) + RPAREN


class Not(Grammar, ExpressionAction):

    grammar = Keyword("NOT") + LPAREN + expression_proxy + RPAREN


class Or(Grammar, ExpressionAction):

    grammar = Keyword("OR") + LPAREN + delimited_list(expression_proxy) + RPAREN


class BooleanExpression(Grammar):

    grammar = And | Not | Or
