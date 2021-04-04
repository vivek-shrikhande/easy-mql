from easymql import Grammar
from easymql.core import Keyword, Suppress, Regex, Optional, QuotedString

from easymql.expressions import Expression


class CollectionName(Grammar):

    grammar = QuotedString(quoteChar="'", escChar='\\') | Regex(r'[\w.]+')


class DbName(Grammar):

    grammar = QuotedString(quoteChar="'", escChar='\\') | Regex(r'\w+')


class DbCollectionPath(Grammar):

    grammar = Optional(Keyword('DB') + DbName) + Keyword("COLL") + CollectionName

    @classmethod
    def action(cls, tokens):
        if len(tokens) == 2:
            return tokens[-1]
        else:
            return {'db': tokens[1], 'coll': tokens[-1]}


class Field(Grammar):

    grammar = QuotedString(quoteChar="'", escChar='\\') | Regex(r'[\w.]+')


class Alias(Grammar):

    grammar = Expression + Suppress(Keyword("AS")) + Field

    @classmethod
    def action(cls, tokens):
        return {tokens[1]: tokens[0]}
