from functools import reduce

from pyparsing import QuotedString

from easymql import Grammar
from easymql.basics import *
from easymql.proxies import data_type_proxy
from easymql.utils import delimited_list


class Array(Grammar):

    grammar = LBRACK + delimited_list(data_type_proxy, min=0, max=...) + RBRACK

    @staticmethod
    def action(tokens):
        return [tokens.asList()]


class KeyValuePair(Grammar):

    grammar = QuotedString(quoteChar='"', escChar='\\') + COLON + data_type_proxy

    @staticmethod
    def action(tokens):
        return {tokens[0]: tokens[1]}


class Object(Grammar):

    grammar = LBRACE + delimited_list(KeyValuePair(), min=0, max=...) + RBRACE

    @staticmethod
    def action(tokens):
        return reduce(lambda e1, e2: {**e1, **e2}, tokens) if tokens else {}