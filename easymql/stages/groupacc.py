from easymql import Grammar
from easymql.actions import ExpressionAction
from easymql.basics import LPAREN, RPAREN
from easymql.core import Keyword
from easymql.expressions import Expression


class AddToSet(Grammar, ExpressionAction):

    grammar = Keyword("ADD_TO_SET") + LPAREN + Expression + RPAREN


class Avg(Grammar, ExpressionAction):

    grammar = Keyword("AVG") + LPAREN + Expression + RPAREN


class First(Grammar, ExpressionAction):

    grammar = Keyword('FIRST') + LPAREN + Expression + RPAREN


class Last(Grammar, ExpressionAction):

    grammar = Keyword('LAST') + LPAREN + Expression + RPAREN


class Max(Grammar, ExpressionAction):

    grammar = Keyword("MAX") + LPAREN + Expression + RPAREN


class MergeObjects(Grammar, ExpressionAction):

    grammar = Keyword("MERGE_OBJECTS") + LPAREN + Expression + RPAREN


class Min(Grammar, ExpressionAction):

    grammar = Keyword("MIN") + LPAREN + Expression + RPAREN


class Push(Grammar, ExpressionAction):

    grammar = Keyword("PUSH") + LPAREN + Expression + RPAREN


class StdDevPop(Grammar, ExpressionAction):

    grammar = Keyword("STD_DEV_POP") + LPAREN + Expression + RPAREN


class StdDevSamp(Grammar, ExpressionAction):

    grammar = Keyword("STD_DEV_SAMP") + LPAREN + Expression + RPAREN


class Sum(Grammar, ExpressionAction):

    grammar = Keyword("SUM") + LPAREN + Expression + RPAREN


class GroupByAccumulatorExpression(Grammar):

    grammar = (
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
