from easymql import Grammar
from easymql.actions import ExpressionAction
from easymql.basics import LPAREN, RPAREN, COMMA
from easymql.core import Keyword, MatchFirst, Optional, Suppress
from easymql.keywords import (
    CONCAT,
    INDEX_OF_BYTES,
    INDEX_OF_CP,
    TRIM,
    LTRIM,
    RTRIM,
    REGEX_FIND,
    REGEX_FIND_ALL,
    REGEX_MATCH,
    REPLACE,
    REPLACE_ALL,
    SPLIT,
    STR_LEN_BYTES,
    STR_LEN_CP,
    STRCASECMP,
    SUBSTR,
    SUBSTR_BYTES,
    SUBSTR_CP,
    TO_LOWER,
    TO_UPPER,
)
from easymql.proxies import expression_proxy
from easymql.utils import delimited_list


class Concat(Grammar, ExpressionAction):

    grammar = CONCAT + LPAREN + delimited_list(expression_proxy, min=2) + RPAREN


class IndexOfBytes(Grammar, ExpressionAction):

    grammar = INDEX_OF_BYTES + LPAREN + delimited_list(expression_proxy, min=2, max=4) + RPAREN


class IndexOfCP(Grammar, ExpressionAction):

    grammar = INDEX_OF_CP + LPAREN + delimited_list(expression_proxy, min=2, max=4) + RPAREN

    @staticmethod
    def action(tokens):
        return {
            '$indexOfCP': tokens[1:]
        }


class Trim(Grammar, ExpressionAction):

    grammar = TRIM + LPAREN + delimited_list(expression_proxy, min=1, max=2) + RPAREN

    @staticmethod
    def action(tokens):
        return {
            '$trim': dict(
                zip(('input', 'chars'), tokens[1:])
            )
        }


class LTrim(Grammar, ExpressionAction):

    grammar = LTRIM + LPAREN + delimited_list(expression_proxy, min=1, max=2) + RPAREN

    @staticmethod
    def action(tokens):
        return {
            '$ltrim': dict(
                zip(('input', 'chars'), tokens[1:])
            )
        }


class RTrim(Grammar, ExpressionAction):

    grammar = RTRIM + LPAREN + delimited_list(expression_proxy, min=1, max=2) + RPAREN

    @staticmethod
    def action(tokens):
        return {
            '$rtrim': dict(
                zip(('input', 'chars'), tokens[1:])
            )
        }


class RegexFind(Grammar):

    grammar = (
        REGEX_FIND
        + LPAREN
        + expression_proxy
        + COMMA
        + expression_proxy
        + Optional(COMMA + expression_proxy)
        + RPAREN
    )

    @staticmethod
    def action(tokens):
        return {
            '$regexFind': dict(
                zip(('input', 'regex', 'options'), tokens[1:])
            )
        }


class RegexFindAll(Grammar):

    grammar = (
        REGEX_FIND_ALL
        + LPAREN
        + expression_proxy
        + COMMA
        + expression_proxy
        + Optional(COMMA + expression_proxy)
        + RPAREN
    )

    @staticmethod
    def action(tokens):
        return {
            '$regexFindAll': dict(
                zip(('input', 'regex', 'options'), tokens[1:])
            )
        }


class RegexMatch(Grammar):

    grammar = (
        REGEX_MATCH
        + LPAREN
        + expression_proxy
        + COMMA
        + expression_proxy
        + Optional(COMMA + expression_proxy)
        + RPAREN
    )

    @staticmethod
    def action(tokens):
        return {
            '$regexMatch': dict(
                zip(('input', 'regex', 'options'), tokens[1:])
            )
        }


class Replace(Grammar):

    grammar = (
        REPLACE
        + LPAREN
        + delimited_list(expression_proxy, min=3, max=3)
        + RPAREN
    )

    @staticmethod
    def action(tokens):
        return {
            '$replaceOne': dict(
                zip(('input', 'find', 'replacement'), tokens[1:])
            )
        }


class ReplaceAll(Grammar):

    grammar = (
        REPLACE_ALL
        + LPAREN
        + delimited_list(expression_proxy, min=3, max=3)
        + RPAREN
    )

    @staticmethod
    def action(tokens):
        return {
            '$replaceAll': dict(
                zip(('input', 'find', 'replacement'), tokens[1:])
            )
        }


class Split(Grammar, ExpressionAction):

    grammar = SPLIT + LPAREN + delimited_list(expression_proxy, min=2, max=2) + RPAREN


class StringLenght(Grammar, ExpressionAction):

    grammar = STR_LEN_BYTES + LPAREN + expression_proxy + RPAREN

    @staticmethod
    def action(tokens):
        return {
            '$strLenBytes': tokens[1]
        }


class StringLenghtCP(Grammar, ExpressionAction):

    grammar = STR_LEN_CP + LPAREN + expression_proxy + RPAREN

    @staticmethod
    def action(tokens):
        return {
            '$strLenCP': tokens[1]
        }


class Strcasecmp(Grammar, ExpressionAction):

    grammar = STRCASECMP + LPAREN + delimited_list(expression_proxy, min=2, max=2) + RPAREN


class Substr(Grammar, ExpressionAction):

    grammar = SUBSTR + LPAREN + delimited_list(expression_proxy, min=3, max=3) + RPAREN


class SubstrBytes(Grammar, ExpressionAction):

    grammar = SUBSTR_BYTES + LPAREN + delimited_list(expression_proxy, min=3, max=3) + RPAREN


class SubstrCP(Grammar, ExpressionAction):

    grammar = SUBSTR_CP + LPAREN + delimited_list(expression_proxy, min=3, max=3) + RPAREN

    @staticmethod
    def action(tokens):
        return {
            '$substrCP': tokens[1:]
        }


class toLower(Grammar, ExpressionAction):

    grammar = TO_LOWER + LPAREN + expression_proxy + RPAREN


class toUpper(Grammar, ExpressionAction):

    grammar = TO_UPPER + LPAREN + expression_proxy + RPAREN


StringExpression = (
    Concat
    | IndexOfBytes
    | IndexOfCP
    | Trim
    | LTrim
    | RTrim
    | RegexFind
    | RegexFindAll
    | RegexMatch
    | Replace
    | ReplaceAll
    | Split
    | StringLenght
    | StringLenghtCP
    | Strcasecmp
    | Substr
    | SubstrBytes
    | SubstrCP
    | toLower
    | toUpper
)
