from easymql.core import Suppress, Regex, Optional, QuotedString
from easymql.expressions import Expression
from easymql.keywords import DB, COLL, AS
from easymql.meta import Grammar
from easymql.stages.groupacc import GroupByAccumulatorExpression


class CollectionName(Grammar):

    grammar = QuotedString(quoteChar="'", escChar='\\') | Regex(r'[\w.]+')


class DbName(Grammar):

    grammar = QuotedString(quoteChar="'", escChar='\\') | Regex(r'\w+')


class DbCollectionPath(Grammar):

    grammar = Optional(DB + DbName) + COLL + CollectionName

    @classmethod
    def action(cls, tokens):
        if len(tokens) == 2:
            return tokens[-1]
        else:
            return {'db': tokens[1], 'coll': tokens[-1]}


class Field(Grammar):

    grammar = QuotedString(quoteChar="'", escChar='\\') | Regex(r'[\w.]+')


class Alias(Grammar):

    grammar = Expression + Suppress(AS) + Field

    @classmethod
    def action(cls, tokens):
        return {tokens[1]: tokens[0]}


class ProjectAccumulator(Grammar):

    grammar = GroupByAccumulatorExpression + AS + Field

    @classmethod
    def action(cls, tokens):
        return {tokens[-1]: tokens[0]}
