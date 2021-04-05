from easymql import Grammar
from easymql.actions import ExpressionAction
from easymql.basics import LPAREN, RPAREN
from easymql.expressions import Expression
from easymql.keywords import (
    ADD_TO_SET,
    AVG,
    FIRST,
    LAST,
    MAX,
    MERGE_OBJECTS,
    MIN,
    PUSH,
    STD_DEV_POP,
    STD_DEV_SAMP,
    SUM,
)


class AddToSet(Grammar, ExpressionAction):

    grammar = ADD_TO_SET + LPAREN + Expression + RPAREN


class Avg(Grammar, ExpressionAction):

    grammar = AVG + LPAREN + Expression + RPAREN


class First(Grammar, ExpressionAction):

    grammar = FIRST + LPAREN + Expression + RPAREN


class Last(Grammar, ExpressionAction):

    grammar = LAST + LPAREN + Expression + RPAREN


class Max(Grammar, ExpressionAction):

    grammar = MAX + LPAREN + Expression + RPAREN


class MergeObjects(Grammar, ExpressionAction):

    grammar = MERGE_OBJECTS + LPAREN + Expression + RPAREN


class Min(Grammar, ExpressionAction):

    grammar = MIN + LPAREN + Expression + RPAREN


class Push(Grammar, ExpressionAction):

    grammar = PUSH + LPAREN + Expression + RPAREN


class StdDevPop(Grammar, ExpressionAction):

    grammar = STD_DEV_POP + LPAREN + Expression + RPAREN


class StdDevSamp(Grammar, ExpressionAction):

    grammar = STD_DEV_SAMP + LPAREN + Expression + RPAREN


class Sum(Grammar, ExpressionAction):

    grammar = SUM + LPAREN + Expression + RPAREN


GroupByAccumulatorExpression = (
    AddToSet
    | Avg
    | First
    | Last
    | Max
    | MergeObjects
    | Min
    | Push
    | StdDevPop
    | StdDevSamp
    | Sum
)
