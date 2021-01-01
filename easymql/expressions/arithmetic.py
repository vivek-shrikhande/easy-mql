from pyparsing import Keyword

from easymql import Grammar
from easymql.actions import ExpressionAction
from easymql.basics import LPAREN, RPAREN
from easymql.proxies import expression_proxy
from easymql.utils import delimited_list


class Abs(Grammar, ExpressionAction):

    grammar = Keyword("ABS") + LPAREN + expression_proxy + RPAREN


class Add(Grammar, ExpressionAction):

    grammar = Keyword("ADD") + LPAREN + delimited_list(expression_proxy) + RPAREN


class Ceil(Grammar, ExpressionAction):

    grammar = Keyword("CEIL") + LPAREN + expression_proxy + RPAREN


class Divide(Grammar, ExpressionAction):

    grammar = (
        Keyword("DIVIDE")
        + LPAREN
        + delimited_list(expression_proxy, min=2, max=2)
        + RPAREN
    )


class Exp(Grammar, ExpressionAction):

    grammar = Keyword("EXP") + LPAREN + expression_proxy + RPAREN


class Floor(Grammar, ExpressionAction):

    grammar = Keyword("FLOOR") + LPAREN + expression_proxy + RPAREN


class Ln(Grammar, ExpressionAction):

    grammar = Keyword("LN") + LPAREN + expression_proxy + RPAREN


class Log(Grammar, ExpressionAction):

    grammar = (
        Keyword("LOG")
        + LPAREN
        + delimited_list(expression_proxy, min=2, max=2)
        + RPAREN
    )


class Log10(Grammar, ExpressionAction):

    grammar = Keyword("LOG10") + LPAREN + expression_proxy + RPAREN


class Mod(Grammar, ExpressionAction):

    grammar = (
        Keyword("MOD")
        + LPAREN
        + delimited_list(expression_proxy, min=2, max=2)
        + RPAREN
    )


class Multiply(Grammar, ExpressionAction):

    grammar = Keyword("MULTIPLY") + LPAREN + delimited_list(expression_proxy) + RPAREN


class Pow(Grammar, ExpressionAction):

    grammar = (
        Keyword("POW")
        + LPAREN
        + delimited_list(expression_proxy, min=2, max=2)
        + RPAREN
    )


class Round(Grammar, ExpressionAction):

    grammar = (
        Keyword("ROUND")
        + LPAREN
        + delimited_list(expression_proxy, min=1, max=2)
        + RPAREN
    )


class Sqrt(Grammar, ExpressionAction):

    grammar = Keyword("SQRT") + LPAREN + expression_proxy + RPAREN


class Subtract(Grammar, ExpressionAction):

    grammar = (
        Keyword("SUBTRACT")
        + LPAREN
        + delimited_list(expression_proxy, min=2, max=2)
        + RPAREN
    )


class Trunc(Grammar, ExpressionAction):

    grammar = (
        Keyword("TRUNC")
        + LPAREN
        + delimited_list(expression_proxy, min=1, max=2)
        + RPAREN
    )


class ArithmeticExpression(Grammar):

    grammar = (
        Abs()
        | Add()
        | Ceil()
        | Divide()
        | Exp()
        | Floor()
        | Ln()
        | Log()
        | Log10()
        | Mod()
        | Multiply()
        | Pow()
        | Round()
        | Sqrt()
        | Subtract()
        | Trunc()
    )
