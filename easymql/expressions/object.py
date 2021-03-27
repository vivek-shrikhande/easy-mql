from easymql.core import Keyword

from easymql import Grammar
from easymql.actions import ExpressionAction
from easymql.basics import LPAREN, RPAREN
from easymql.proxies import expression_proxy
from easymql.utils import delimited_list


class MergeObjects(Grammar, ExpressionAction):

    grammar = (
        Keyword("MERGE_OBJECTS") + LPAREN + delimited_list(expression_proxy) + RPAREN
    )


class ObjectToArray(Grammar):

    grammar = Keyword("OBJECT_TO_ARRAY") + LPAREN + expression_proxy + RPAREN

    @classmethod
    def action(cls, tokens):
        return {'$objectToArray': tokens[1]}
