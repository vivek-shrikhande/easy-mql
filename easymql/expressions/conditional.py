from pyparsing import Keyword, Optional, Suppress, White

from easymql import Grammar
from easymql.actions import ExpressionAction
from easymql.basics import LPAREN, RPAREN
from easymql.proxies import expression_proxy
from easymql.utils import delimited_list


class Cond(Grammar):

    grammar = (
        Suppress(Keyword("IF"))
        + LPAREN
        + delimited_list(expression_proxy, min=3, max=3)
        + RPAREN
    )

    @staticmethod
    def action(tokens):
        return {"$cond": {"if": tokens[0], "then": tokens[1], "else": tokens[2]}}


class IfNull(Grammar, ExpressionAction):

    grammar = (
        Keyword("IF_NULL")
        + LPAREN
        + delimited_list(expression_proxy, min=2, max=2)
        + RPAREN
    )


class Case(Grammar):

    grammar = (
        Suppress(Keyword("CASE"))
        + delimited_list(
            Suppress(Keyword("WHEN"))
            + expression_proxy
            + Suppress(Keyword("THEN"))
            + expression_proxy,
            delimiter=White(),
            min=1,
        )
        + Optional(Suppress(Keyword("ELSE")) + expression_proxy)
        + Suppress(Keyword("END"))
    )

    @staticmethod
    def action(tokens):
        res = {"$switch": {}}
        tokens = tokens.asList()

        if len(tokens) % 2 == 1:
            res["$switch"]["default"] = tokens.pop()

        i = 0
        branches = list()
        while i < len(tokens):
            b = {"case": tokens[i], "then": tokens[i + 1]}
            print(b)
            branches.append(b)
            i = i + 2
        res["$switch"]["branches"] = branches

        return res


class ConditionalExpression(Grammar):

    grammar = Cond() | IfNull() | Case()
