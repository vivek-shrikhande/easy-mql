from easymql.core import Keyword, Optional, Suppress, Word
from pyparsing import alphanums
from easymql import Grammar
from easymql.datatypes.composite import Array
from easymql.actions import ExpressionAction
from easymql.basics import LPAREN, RPAREN
from easymql.proxies import expression_proxy
from easymql.utils import delimited_list


class ArrayElemAt(Grammar, ExpressionAction):

    grammar = (
        Keyword('ARRAY_ELEM_AT')
        + LPAREN
        + delimited_list(expression_proxy, min=2, max=2)
        + RPAREN
    )


class ArrayToObject(Grammar, ExpressionAction):

    grammar = Keyword('ARRAY_TO_OBJECT') + LPAREN + expression_proxy + RPAREN


class ConcatArrays(Grammar, ExpressionAction):

    grammar = (
        Keyword('CONCAT_ARRAYS')
        + LPAREN
        + delimited_list(expression_proxy, min=2, max=...)
        + RPAREN
    )


class Filter(Grammar, ExpressionAction):
    grammar = (
        Suppress(Keyword("FILTER"))
        + LPAREN
        + delimited_list(expression_proxy, min=3, max=3)
        + RPAREN
    )

    @staticmethod
    def action(tokens):
        return {"$filter": {"input": tokens[0], "as": tokens[1], "cond": tokens[2]}}


class First(Grammar, ExpressionAction):

    grammar = Keyword('FIRST') + LPAREN + expression_proxy + RPAREN


class In(Grammar, ExpressionAction):

    grammar = (
        Keyword('IN') + LPAREN + delimited_list(expression_proxy, min=2, max=2) + RPAREN
    )


class IndexOfArray(Grammar, ExpressionAction):

    grammar = (
        Keyword('INDEX_OF_ARRAY')
        + LPAREN
        + delimited_list(expression_proxy, min=2, max=4)
        + RPAREN
    )


class IsArray(Grammar, ExpressionAction):

    grammar = Keyword('IS_ARRAY') + LPAREN + expression_proxy + RPAREN


class Last(Grammar, ExpressionAction):

    grammar = Keyword('LAST') + LPAREN + expression_proxy + RPAREN


class Map(Grammar, ExpressionAction):
    grammar = (
        Suppress(Keyword("MAP"))
        + LPAREN
        + delimited_list(expression_proxy, min=3, max=3)
        + RPAREN
    )

    @staticmethod
    def action(tokens):
        return {"$map": {"input": tokens[0], "as": tokens[1], "in": tokens[2]}}


class ObjectToArray(Grammar, ExpressionAction):

    grammar = Suppress(Keyword("OBJECT_TO_ARRAY")) + LPAREN + expression_proxy + RPAREN

    @staticmethod
    def action(tokens):
        return {"$objectToArray": tokens[0]}


class Range(Grammar, ExpressionAction):

    grammar = (
        Keyword('RANGE')
        + LPAREN
        + delimited_list(expression_proxy, min=2, max=3)
        + RPAREN
    )


class Reduce(Grammar, ExpressionAction):
    grammar = (
        Suppress(Keyword("REDUCE"))
        + LPAREN
        + delimited_list(expression_proxy, min=3, max=3)
        + RPAREN
    )

    @staticmethod
    def action(tokens):
        return {
            "$reduce": {"input": tokens[0], "initialValue": tokens[1], "in": tokens[2]}
        }


class ReverseArray(Grammar, ExpressionAction):

    grammar = Keyword('REVERSE_ARRAY') + LPAREN + expression_proxy + RPAREN


class Size(Grammar, ExpressionAction):

    grammar = Keyword('SIZE') + LPAREN + expression_proxy + RPAREN


class Slice(Grammar, ExpressionAction):

    grammar = (
        Keyword("SLICE")
        + LPAREN
        + delimited_list(expression_proxy, min=2, max=3)
        + RPAREN
    )


class Zip(Grammar, ExpressionAction):
    grammar = (
        Suppress(Keyword("ZIP"))
        + LPAREN
        + delimited_list(expression_proxy, min=1, max=3)
        + RPAREN
    )

    @staticmethod
    def action(tokens):

        result = {"inputs": tokens[0]}
        if len(tokens) >= 2:
            result["useLongestLength"] = tokens[1]

        if len(tokens) == 3:
            result["defaults"] = tokens[2]

        return {"$zip": result}


class ArrayExpression(Grammar):

    grammar = (
        ArrayElemAt
        | ArrayToObject
        | ConcatArrays
        | Filter
        | First
        | In
        | IndexOfArray
        | IsArray
        | Last
        | Map
        | ObjectToArray
        | Range
        | Reduce
        | ReverseArray
        | Size
        | Slice
        | Zip
    )
