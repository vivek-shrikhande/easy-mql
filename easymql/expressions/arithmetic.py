from easymql import Grammar
from easymql.actions import ExpressionAction
from easymql.basics import LPAREN, RPAREN
from easymql.keywords import (
    ABS,
    ADD,
    CEIL,
    DIVIDE,
    EXP,
    FLOOR,
    LN,
    LOG,
    LOG10,
    MOD,
    MULTIPLY,
    POW,
    ROUND,
    SQRT,
    SUBTRACT,
    TRUNC,
)
from easymql.proxies import expression_proxy
from easymql.utils import delimited_list


class Abs(Grammar, ExpressionAction):

    grammar = ABS + LPAREN + expression_proxy + RPAREN


class Add(Grammar, ExpressionAction):

    grammar = ADD + LPAREN + delimited_list(expression_proxy) + RPAREN


class Ceil(Grammar, ExpressionAction):

    grammar = CEIL + LPAREN + expression_proxy + RPAREN


class Divide(Grammar, ExpressionAction):

    grammar = DIVIDE + LPAREN + delimited_list(expression_proxy, min=2, max=2) + RPAREN


class Exp(Grammar, ExpressionAction):

    grammar = EXP + LPAREN + expression_proxy + RPAREN


class Floor(Grammar, ExpressionAction):

    grammar = FLOOR + LPAREN + expression_proxy + RPAREN


class Ln(Grammar, ExpressionAction):

    grammar = LN + LPAREN + expression_proxy + RPAREN


class Log(Grammar, ExpressionAction):

    grammar = LOG + LPAREN + delimited_list(expression_proxy, min=2, max=2) + RPAREN


class Log10(Grammar, ExpressionAction):

    grammar = LOG10 + LPAREN + expression_proxy + RPAREN


class Mod(Grammar, ExpressionAction):

    grammar = MOD + LPAREN + delimited_list(expression_proxy, min=2, max=2) + RPAREN


class Multiply(Grammar, ExpressionAction):

    grammar = MULTIPLY + LPAREN + delimited_list(expression_proxy) + RPAREN


class Pow(Grammar, ExpressionAction):

    grammar = POW + LPAREN + delimited_list(expression_proxy, min=2, max=2) + RPAREN


class Round(Grammar, ExpressionAction):

    grammar = ROUND + LPAREN + delimited_list(expression_proxy, min=1, max=2) + RPAREN


class Sqrt(Grammar, ExpressionAction):

    grammar = SQRT + LPAREN + expression_proxy + RPAREN


class Subtract(Grammar, ExpressionAction):

    grammar = (
        SUBTRACT + LPAREN + delimited_list(expression_proxy, min=2, max=2) + RPAREN
    )


class Trunc(Grammar, ExpressionAction):

    grammar = TRUNC + LPAREN + delimited_list(expression_proxy, min=1, max=2) + RPAREN


ArithmeticExpression = (
    Abs
    | Add
    | Ceil
    | Divide
    | Exp
    | Floor
    | Ln
    | Log
    | Log10
    | Mod
    | Multiply
    | Pow
    | Round
    | Sqrt
    | Subtract
    | Trunc
)
