from easymql import Grammar
from easymql.actions import ExpressionAction
from easymql.basics import LPAREN, RPAREN
from easymql.keywords import AVG, MAX, MIN, STD_DEV_POP, STD_DEV_SAMP, SUM
from easymql.proxies import expression_proxy
from easymql.utils import delimited_list


class Avg(Grammar, ExpressionAction):

    grammar = AVG + LPAREN + delimited_list(expression_proxy, min=1, max=...) + RPAREN


class Max(Grammar, ExpressionAction):

    grammar = MAX + LPAREN + delimited_list(expression_proxy, min=1, max=...) + RPAREN


class Min(Grammar, ExpressionAction):

    grammar = MIN + LPAREN + delimited_list(expression_proxy, min=1, max=...) + RPAREN


class StdDevPop(Grammar, ExpressionAction):

    grammar = (
        STD_DEV_POP + LPAREN + delimited_list(expression_proxy, min=1, max=...) + RPAREN
    )


class StdDevSamp(Grammar, ExpressionAction):

    grammar = (
        STD_DEV_SAMP
        + LPAREN
        + delimited_list(expression_proxy, min=1, max=...)
        + RPAREN
    )


class Sum(Grammar, ExpressionAction):

    grammar = SUM + LPAREN + delimited_list(expression_proxy, min=1, max=...) + RPAREN


AccumulatorExpression = Avg | Max | Min | StdDevPop | StdDevSamp | Sum
