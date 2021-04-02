from easymql import Grammar
from easymql.core import QuotedString, Regex


class FieldPath(Grammar):

    grammar = QuotedString(quoteChar="'", escChar='\\') | Regex(r'[\w.]+')

    @classmethod
    def action(cls, token):
        return '$' + token[0]
