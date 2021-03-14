from easymql.core import Keyword

from easymql import Grammar
from easymql.actions import ExpressionAction
from easymql.basics import LPAREN, RPAREN
from easymql.proxies import expression_proxy


class IsNumber(Grammar, ExpressionAction):

    grammar = Keyword('IS_NUMBER') + LPAREN + expression_proxy + RPAREN


class ToBool(Grammar, ExpressionAction):

    grammar = Keyword('TO_BOOL') + LPAREN + expression_proxy + RPAREN


class ToDate(Grammar, ExpressionAction):

    grammar = Keyword('TO_DATE') + LPAREN + expression_proxy + RPAREN


class ToDecimal(Grammar, ExpressionAction):

    grammar = Keyword('TO_DECIMAL') + LPAREN + expression_proxy + RPAREN


class ToDouble(Grammar, ExpressionAction):

    grammar = Keyword('TO_DOUBLE') + LPAREN + expression_proxy + RPAREN


class ToInt(Grammar, ExpressionAction):

    grammar = Keyword('TO_INT') + LPAREN + expression_proxy + RPAREN


class ToLong(Grammar, ExpressionAction):

    grammar = Keyword('TO_LONG') + LPAREN + expression_proxy + RPAREN


class ToObjectId(Grammar, ExpressionAction):

    grammar = Keyword('TO_OBJECT_ID') + LPAREN + expression_proxy + RPAREN


class ToString(Grammar, ExpressionAction):

    grammar = Keyword('TO_STRING') + LPAREN + expression_proxy + RPAREN


class Type(Grammar, ExpressionAction):

    grammar = Keyword('TYPE') + LPAREN + expression_proxy + RPAREN


class TypeExpression(Grammar):

    grammar = (
        IsNumber
        | ToBool
        | ToDate
        | ToDecimal
        | ToDouble
        | ToInt
        | ToLong
        | ToObjectId
        | ToString
        | Type
    )
