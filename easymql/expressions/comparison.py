from easymql import Grammar
from easymql.actions import ExpressionAction
from easymql.basics import LPAREN, RPAREN
from easymql.keywords import CMP
from easymql.proxies import expression_proxy
from easymql.utils import delimited_list


class Cmp(Grammar, ExpressionAction):

    grammar = CMP + LPAREN + delimited_list(expression_proxy, min=2, max=2) + RPAREN
