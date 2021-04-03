from easymql import Grammar
from easymql.actions import ExpressionAction
from easymql.basics import LPAREN, RPAREN
from easymql.core import Keyword
from easymql.proxies import expression_proxy
from easymql.utils import delimited_list


class AddToSet(Grammar, ExpressionAction):

    grammar = Keyword("ADD_TO_SET") + LPAREN + expression_proxy + RPAREN


class Avg(Grammar, ExpressionAction):

    grammar = (
        Keyword("AVG")
        + LPAREN
        + delimited_list(expression_proxy, min=1, max=...)
        + RPAREN
    )


class Max(Grammar, ExpressionAction):

    grammar = (
        Keyword("MAX")
        + LPAREN
        + delimited_list(expression_proxy, min=1, max=...)
        + RPAREN
    )


class Min(Grammar, ExpressionAction):

    grammar = (
        Keyword("MIN")
        + LPAREN
        + delimited_list(expression_proxy, min=1, max=...)
        + RPAREN
    )


class Push(Grammar, ExpressionAction):

    grammar = Keyword("PUSH") + LPAREN + expression_proxy + RPAREN


class StdDevPop(Grammar, ExpressionAction):

    grammar = (
        Keyword("STD_DEV_POP")
        + LPAREN
        + delimited_list(expression_proxy, min=1, max=...)
        + RPAREN
    )


class StdDevSamp(Grammar, ExpressionAction):

    grammar = (
        Keyword("STD_DEV_SAMP")
        + LPAREN
        + delimited_list(expression_proxy, min=1, max=...)
        + RPAREN
    )


class Sum(Grammar, ExpressionAction):

    grammar = (
        Keyword("SUM")
        + LPAREN
        + delimited_list(expression_proxy, min=1, max=...)
        + RPAREN
    )


class AccumulatorExpression(Grammar):

    grammar = AddToSet | Avg | Max | Min | Push | StdDevPop | StdDevSamp | Sum
