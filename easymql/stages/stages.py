from functools import reduce

from pyparsing import ParseException

from easymql import Grammar
from easymql.basics import SEMICOLON, RPAREN, LPAREN
from easymql.core import Keyword, Suppress, Literal, Optional
from easymql.datatypes.primary import Number, Boolean
from easymql.expressions import Expression
from easymql.expressions.others import FieldPath
from easymql.stages.parts import CollectionName, DbCollectionPath, Field, Alias
from easymql.utils import delimited_list, keyword_group


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
        + DbCollectionPath
        + SEMICOLON
    )

    @classmethod
    def action(cls, tokens):
        return {"$out": tokens[0]}


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


class Sort(Grammar):
    class PairBySort(Grammar):
        grammar = Field + (Keyword('ASC') | Keyword('DESC'))

        @classmethod
        def action(cls, tokens):
            if tokens[1] == "ASC":
                tokens[1] = 1
            elif tokens[1] == 'DESC':
                tokens[1] = -1
            return {tokens[0]: tokens[1]}

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


class Unwind(Grammar):
    class ArrayIndex(Grammar):
        grammar = Keyword("ARRAY") + Keyword("INDEX") + Keyword("AS") + Field

        @classmethod
        def action(cls, tokens):
            return 'includeArrayIndex', tokens[-1]

    class PreserverNullEmptyArrays(Grammar):
        grammar = (
            Keyword("PRESERVE")
            + Keyword("NULL")
            + Keyword("EMPTY")
            + Keyword("ARRAYS")
            + Boolean
        )

        @classmethod
        def action(cls, tokens):
            return 'preserveNullAndEmptyArrays', tokens[-1]

    grammar = (
        Keyword("UNWIND")
        + FieldPath
        + (ArrayIndex | PreserverNullEmptyArrays)[0, 2]
        + SEMICOLON
    )

    @classmethod
    def action(cls, loc, tokens):
        # raise error if 2 options are given but both are the same
        if len(tokens) == 4 and tokens[2][0] == tokens[3][0]:
            if tokens[2][0] == 'includeArrayIndex':
                option = 'ARRAY INDEX AS'
            else:
                option = 'PRESERVE NULL EMPTY ARRAYS'
            raise ParseException('', loc=loc, msg=f"Duplicate option '{option}'")
        return {'$unwind': dict([('path', tokens[1])] + tokens[2:])}


class Merge(Grammar):
    class On(Grammar):
        grammar = Keyword('ON') + delimited_list(Field, min=1)

        @classmethod
        def action(cls, tokens):
            print(tokens.asList())
            return {'on': tokens[1:]}

    class WhenMatched(Grammar):
        grammar = Suppress(keyword_group('WHEN MATCHED THEN')) + (
            Keyword('REPLACE')
            | Keyword('KEEP')
            | Keyword('MERGE')
            | Keyword('FAIL')
            | LPAREN
            + (AddFields | Set | Project | Unset | ReplaceRoot | ReplaceWith)[1, ...]
            + RPAREN
        )

        @classmethod
        def action(cls, tokens):
            value = tokens.asList()
            if isinstance(tokens[0], str):
                if tokens[0] == 'KEEP':
                    value = 'keepExisting'
                else:
                    value = tokens[0].lower()
            return {'whenMatched': value}

    class WhenNotMatched(Grammar):
        grammar = Suppress(keyword_group('WHEN NOT MATCHED THEN')) + (
            Keyword('INSERT') | Keyword('DISCARD') | Keyword('FAIL')
        )

        @classmethod
        def action(cls, tokens):
            return {'whenNotMatched': tokens[0].lower()}

    grammar = (
        Keyword('MERGE')
        + Keyword('INTO')
        + DbCollectionPath
        + Optional(On)
        + Optional(WhenMatched)
        + Optional(WhenNotMatched)
        + SEMICOLON
    )

    @classmethod
    def action(cls, tokens):
        return {
            '$merge': reduce(
                lambda x, y: {**x, **y}, [{'into': tokens[2]}] + tokens[3:]
            )
        }


Stages = (
    AddFields
    | Count
    | Limit
    | Lookup
    | Match
    | Merge
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
    | Unwind
)