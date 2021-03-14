from easymql.core import Keyword

from easymql import Grammar
from easymql.actions import ExpressionAction
from easymql.basics import LPAREN, RPAREN
from easymql.datatypes.composite import Array
from easymql.utils import delimited_list


class AllElementsTrue(Grammar, ExpressionAction):

    grammar = Keyword('ALL_ELEMENTS_TRUE') + LPAREN + Array + RPAREN


class AnyElementTrue(Grammar, ExpressionAction):

    grammar = Keyword('ANY_ELEMENT_TRUE') + LPAREN + Array + RPAREN


class SetDifference(Grammar, ExpressionAction):

    grammar = (
        Keyword('SET_DIFFERENCE')
        + LPAREN
        + delimited_list(Array, min=2, max=2)
        + RPAREN
    )


class SetEquals(Grammar, ExpressionAction):

    grammar = Keyword('SET_EQUALS') + LPAREN + delimited_list(Array) + RPAREN


class SetIntersection(Grammar, ExpressionAction):

    grammar = Keyword('SET_INTERSECTION') + LPAREN + delimited_list(Array) + RPAREN


class SetIsSubset(Grammar, ExpressionAction):

    grammar = (
        Keyword('SET_IS_SUBSET') + LPAREN + delimited_list(Array, min=2, max=2) + RPAREN
    )


class SetUnion(Grammar, ExpressionAction):

    grammar = Keyword('SET_UNION') + LPAREN + delimited_list(Array) + RPAREN


class SetExpression(Grammar):

    grammar = (
        AllElementsTrue
        | AnyElementTrue
        | SetDifference
        | SetEquals
        | SetIntersection
        | SetIsSubset
        | SetUnion
    )
