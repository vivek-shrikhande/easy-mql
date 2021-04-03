from pyparsing import alphanums

from easymql import Grammar
from easymql.basics import SEMICOLON
from easymql.core import Keyword, Word, Suppress, Literal, Regex
from easymql.core import Optional
from easymql.core import QuotedString
from easymql.datatypes.primary import Number
from easymql.expressions import Expression
from easymql.utils import delimited_list
from functools import reduce


class CollectionName(Grammar):

    grammar = QuotedString(quoteChar="'", escChar='\\') | Regex(r'[\w.]+')


class Field(Grammar):

    grammar = QuotedString(quoteChar="'", escChar='\\') | Regex(r'[\w.]+')


class Alias(Grammar):

    grammar = Expression + Suppress(Keyword("AS")) + Field

    @classmethod
    def action(cls, tokens):
        return {tokens[1]: tokens[0]}


class AddFields(Grammar):

    grammar = (
        Suppress(Keyword("ADD"))
        + Suppress(Keyword("FIELDS"))
        + delimited_list(Alias, min=1)
        + SEMICOLON
    )

    @classmethod
    def action(cls, tokens):
        fields_dict = {}
        for t in tokens:
            fields_dict.update(t)
        return {"$addFields": fields_dict}


class Count(Grammar):

    grammar = (
        Suppress(Keyword("COUNT"))
        + Suppress(Keyword("AS"))
        + CollectionName
        + SEMICOLON
    )

    @classmethod
    def action(cls, tokens):
        return {"$count": tokens[0]}


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


class OutputToDb(Grammar):

    grammar = (
        Suppress(Keyword("OUTPUT"))
        + Suppress(Keyword("TO"))
        + Optional(Suppress(Keyword("DB")) + Word(alphanums + '_'))
        + Suppress(Keyword("COLL"))
        + CollectionName
        + SEMICOLON
    )

    @classmethod
    def action(cls, tokens):
        if len(tokens) == 1:
            return {"$out": tokens[0]}
        return {"$out": {"db": tokens[0], "coll": tokens[1]}}


class Project(Grammar):
    class NewField(Grammar):
        grammar = Expression + Keyword('AS') + Field

        @classmethod
        def action(cls, tokens):
            return {tokens[-1]: tokens[0]}

    class ExcludeOrInclude(Grammar):
        grammar = Literal('+') + Field | Literal('-') + Field | Field

        @classmethod
        def action(cls, tokens):
            if len(tokens) == 1:
                return {tokens[0]: 1}
            else:
                return {tokens[-1]: 1 if tokens[0] == '+' else 0}

    # order matters
    element = NewField | ExcludeOrInclude
    grammar = Suppress(Keyword("PROJECT")) + delimited_list(element, min=1) + SEMICOLON

    @classmethod
    def action(cls, tokens):
        return {'$project': reduce(lambda x, y: {**x, **y}, tokens)}


class Redact(Grammar):

    grammar = Suppress(Keyword("REDACT")) + Expression + SEMICOLON

    @classmethod
    def action(cls, tokens):
        return {"$redact": tokens[0]}


class ReplaceRoot(Grammar):
    grammar = (
        Suppress(Keyword("REPLACE"))
        + Suppress(Keyword("ROOT"))
        + Expression
        + SEMICOLON
    )

    @classmethod
    def action(cls, tokens):
        return {"$replaceRoot": {"newRoot": tokens[0]}}


class ReplaceWith(Grammar):
    grammar = (
        Suppress(Keyword("REPLACE"))
        + Suppress(Keyword("WITH"))
        + Expression
        + SEMICOLON
    )

    @classmethod
    def action(cls, tokens):
        return {"$replaceWith": tokens[0]}


class Sample(Grammar):

    grammar = Suppress(Keyword("SAMPLE")) + Number + SEMICOLON

    @classmethod
    def action(cls, tokens):
        return {"$sample": tokens[0]}


class Set(Grammar):

    grammar = Suppress(Keyword("SET")) + delimited_list(Alias, min=1) + SEMICOLON

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


class Unset(Grammar):

    grammar = Suppress(Keyword("UNSET")) + delimited_list(Field, min=1) + SEMICOLON

    @classmethod
    def action(cls, tokens):
        token = []
        for i in tokens:
            token.append(i)
        return {"$unset": token}


class Stages(Grammar):

    grammar = (
        AddFields
        | Count
        | Limit
        | Lookup
        | Match
        | Project
        | OutputToDb
        | Redact
        | ReplaceRoot
        | ReplaceWith
        | Sample
        | Set
        | Skip
        | Sort
        | SortByCount
        | Unset
    )
