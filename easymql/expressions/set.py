from easymql import Grammar
from easymql.actions import ExpressionAction
from easymql.basics import LPAREN, RPAREN
from easymql.datatypes.composite import Array
from easymql.keywords import (
    ALL_ELEMENTS_TRUE,
    ANY_ELEMENT_TRUE,
    SET_DIFFERENCE,
    SET_EQUALS,
    SET_UNION,
    SET_INTERSECTION,
    SET_IS_SUBSET,
)
from easymql.utils import delimited_list


class AllElementsTrue(Grammar, ExpressionAction):

    grammar = ALL_ELEMENTS_TRUE + LPAREN + Array + RPAREN


class AnyElementTrue(Grammar, ExpressionAction):

    grammar = ANY_ELEMENT_TRUE + LPAREN + Array + RPAREN


class SetDifference(Grammar, ExpressionAction):

    grammar = SET_DIFFERENCE + LPAREN + delimited_list(Array, min=2, max=2) + RPAREN


class SetEquals(Grammar, ExpressionAction):

    grammar = SET_EQUALS + LPAREN + delimited_list(Array) + RPAREN


class SetIntersection(Grammar, ExpressionAction):

    grammar = SET_INTERSECTION + LPAREN + delimited_list(Array) + RPAREN


class SetIsSubset(Grammar, ExpressionAction):

    grammar = SET_IS_SUBSET + LPAREN + delimited_list(Array, min=2, max=2) + RPAREN


class SetUnion(Grammar, ExpressionAction):

    grammar = SET_UNION + LPAREN + delimited_list(Array) + RPAREN


SetExpression = (
    AllElementsTrue
    | AnyElementTrue
    | SetDifference
    | SetEquals
    | SetIntersection
    | SetIsSubset
    | SetUnion
)
