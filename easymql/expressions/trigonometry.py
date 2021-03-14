from easymql.core import Keyword

from easymql import Grammar
from easymql.actions import ExpressionAction
from easymql.basics import LPAREN, RPAREN
from easymql.proxies import expression_proxy
from easymql.utils import delimited_list


class Sin(Grammar, ExpressionAction):

    grammar = Keyword('SIN') + LPAREN + expression_proxy + RPAREN


class Cos(Grammar, ExpressionAction):

    grammar = Keyword('COS') + LPAREN + expression_proxy + RPAREN


class Tan(Grammar, ExpressionAction):

    grammar = Keyword('TAN') + LPAREN + expression_proxy + RPAREN


class Asin(Grammar, ExpressionAction):

    grammar = Keyword('ASIN') + LPAREN + expression_proxy + RPAREN


class Acos(Grammar, ExpressionAction):

    grammar = Keyword('ACOS') + LPAREN + expression_proxy + RPAREN


class Atan(Grammar, ExpressionAction):

    grammar = Keyword('ATAN') + LPAREN + expression_proxy + RPAREN


class Atan2(Grammar, ExpressionAction):

    grammar = (
        Keyword('ATAN2')
        + LPAREN
        + delimited_list(expression_proxy, min=2, max=2)
        + RPAREN
    )


class Asinh(Grammar, ExpressionAction):

    grammar = Keyword('ASINH') + LPAREN + expression_proxy + RPAREN


class Acosh(Grammar, ExpressionAction):

    grammar = Keyword('ACOSH') + LPAREN + expression_proxy + RPAREN


class Atanh(Grammar, ExpressionAction):

    grammar = Keyword('ATANH') + LPAREN + expression_proxy + RPAREN


class DegreesToRadians(Grammar, ExpressionAction):

    grammar = Keyword('DEGREES_TO_RADIANS') + LPAREN + expression_proxy + RPAREN


class RadiansToDegrees(Grammar, ExpressionAction):

    grammar = Keyword('RADIANS_TO_DEGREES') + LPAREN + expression_proxy + RPAREN


class TrigonometryExpression(Grammar):

    grammar = (
        Sin
        | Cos
        | Tan
        | Asin
        | Acos
        | Atan
        | Atan2
        | Asinh
        | Acosh
        | Atanh
        | DegreesToRadians
        | RadiansToDegrees
    )
