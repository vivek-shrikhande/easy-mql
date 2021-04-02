from pyparsing import alphanums

from easymql import Grammar
from easymql.basics import SEMICOLON
from easymql.core import Keyword, Word, Suppress, Literal, Optional, Regex
from easymql.core import QuotedString
from easymql.datatypes.primary import Number
from easymql.expressions import Expression
from easymql.proxies import expression_proxy
from easymql.utils import delimited_list


class CollectionName(Grammar):

    grammar = QuotedString(quoteChar="'", escChar='\\') | Regex(r'\S+')


class Field(Grammar):

    grammar = QuotedString(quoteChar="'", escChar='\\') | Regex(r'\S+')

    @classmethod
    def action(cls, token):
        return token[0]


class Pair(Grammar):
    grammar = Expression + Suppress(Keyword("AS")) + Word(alphanums + '_')

    @classmethod
    def action(cls, tokens):
        return {tokens[1]: tokens[0]}


class PairBy(Grammar):
    grammar = expression_proxy + Suppress(Keyword("BY")) + Number

    @classmethod
    def action(cls, tokens):
        return {tokens[0]: tokens[1]}


class AddFields(Grammar):
    grammar = (
        Suppress(Keyword("ADD"))
        + Suppress(Keyword("FIELDS"))
        + delimited_list(Pair, min=1)
        + SEMICOLON
    )

    @classmethod
    def action(cls, tokens):
        fields_dict = {}
        for t in tokens:
            fields_dict.update(t)
        return {"$addFields": fields_dict}


class Count(Grammar):

    grammar = Keyword("COUNT") + Keyword("AS") + Word(alphanums + '_') + SEMICOLON

    @classmethod
    def action(cls, tokens):
        return {"$count": tokens[2]}


class Limit(Grammar):

    grammar = Suppress(Keyword("LIMIT")) + Number + SEMICOLON

    @classmethod
    def action(cls, tokens):
        return {"$limit": tokens[0]}


class Lookup(Grammar):

    grammar = (
        Keyword("LOOKUP")
        + CollectionName
        + Keyword("ON")
        + Field
        + Literal('=')
        + Field
        + Optional(Keyword("AS") + Field)
        + SEMICOLON
    )

    @classmethod
    def action(cls, tokens):
        return {
            '$lookup': {
                'from': tokens[1],
                'localField': tokens[3],
                'foreignField': tokens[5],
                'as': tokens[-1] if len(tokens) == 8 else f'{tokens[1]}_docs',
            }
        }


class Match(Grammar):

    grammar = Suppress(Keyword("MATCH")) + Expression + SEMICOLON

    @classmethod
    def action(cls, tokens):
        return {"$match": {"$expr": tokens[0]}}


class Sample(Grammar):

    grammar = Suppress(Keyword("SAMPLE")) + Number + SEMICOLON

    @classmethod
    def action(cls, tokens):
        return {"$sample": tokens[0]}


class Set(Grammar):

    grammar = Suppress(Keyword("SET")) + delimited_list(Pair, min=1) + SEMICOLON

    @classmethod
    def action(cls, tokens):
        fields_dict = {}
        for t in tokens:
            fields_dict.update(t)
        return {"$set": fields_dict}


class Skip(Grammar):

    grammar = (
        (Suppress(Keyword("SKIP")) | Suppress(Keyword("OFFSET"))) + Number + SEMICOLON
    )

    @classmethod
    def action(cls, tokens):
        return {"$skip": tokens[0]}


class PairBySort(Grammar):
    grammar = Field + (Keyword('ASC') | Keyword('DESC'))

    @classmethod
    def action(cls, tokens):
        if tokens[1] == "ASC":
            tokens[1] = 1
        elif tokens[1] == 'DESC':
            tokens[1] = -1
        return {tokens[0]: tokens[1]}


class Sort(Grammar):

    grammar = (
        (Suppress(Keyword("SORT")) | Suppress(Keyword("ORDER")))
        + Suppress(Keyword("BY"))
        + delimited_list(PairBySort, min=1)
        + SEMICOLON
    )

    @classmethod
    def action(cls, tokens):
        fields_dict = {}
        for t in tokens:
            fields_dict.update(t)
        return {"$sort": fields_dict}


class SortByCount(Grammar):

    grammar = (
        Suppress(Keyword("SORT"))
        + Suppress(Keyword("BY"))
        + Suppress(Keyword("COUNT"))
        + Expression
        + SEMICOLON
    )

    @classmethod
    def action(cls, tokens):
        return {"$sortByCount": tokens[0]}


class Stages(Grammar):

    grammar = (
        AddFields
        | Count
        | Limit
        | Lookup
        | Match
        | Sample
        | Set
        | Skip
        | Sort
        | SortByCount
    )
