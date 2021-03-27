from easymql import Grammar
from easymql.core import QuotedString


class FieldPath(Grammar):

    grammar = QuotedString(quoteChar="'", escChar='\\', multiline=True)

    @classmethod
    def action(cls, token):
        return '$' + token[0]
