from pyparsing import (
    Empty as PpEmpty,
    Forward as PpForward,
    Keyword as PpKeyword,
    Literal as PpLiteral,
    Suppress as PpSuppress,
    Word as PpWord,
    QuotedString as PpQuotedString,
    Regex as PpRegex,
    Optional as PpOptional,
    White as PpWhite,
)

from easymql import Adapter


class Keyword(Adapter):
    def __init__(self, match_string):
        grammar = PpKeyword(match_string)
        super(Keyword, self).__init__(grammar)


class Word(Adapter):
    def __init__(
        self,
        initChars,
        bodyChars=None,
        min=1,
        max=0,
        exact=0,
        asKeyword=False,
        excludeChars=None,
    ):
        grammar = PpWord(initChars, bodyChars, min, max, exact, asKeyword, excludeChars)
        super(Word, self).__init__(grammar)


class Suppress(Adapter):
    def __init__(self, expr):
        grammar = PpSuppress(expr._grammar)
        super(Suppress, self).__init__(grammar)


class QuotedString(Adapter):
    def __init__(
        self,
        quoteChar,
        escChar=None,
        escQuote=None,
        multiline=False,
        unquoteResults=True,
        endQuoteChar=None,
        convertWhitespaceEscapes=True,
    ):
        grammar = PpQuotedString(
            quoteChar,
            escChar,
            escQuote,
            multiline,
            unquoteResults,
            endQuoteChar,
            convertWhitespaceEscapes,
        )
        super(QuotedString, self).__init__(grammar)


class Forward(Adapter):
    def __init__(self, other=None):
        grammar = PpForward(other)
        super(Forward, self).__init__(grammar)

    def __lshift__(self, other):
        return Adapter(self.grammar.__lshift__(other._grammar))

    def __ilshift__(self, other):
        return Adapter(self.grammar.__ilshift__(other._grammar))


class Regex(Adapter):
    def __init__(self, pattern, flags=0, asGroupList=False, asMatch=False):
        grammar = PpRegex(pattern, flags, asGroupList, asMatch)
        super(Regex, self).__init__(grammar)


class Empty(Adapter):
    def __init__(self):
        super(Empty, self).__init__(PpEmpty)


class Literal(Adapter):
    def __init__(self, match_string):
        super(Literal, self).__init__(PpLiteral(match_string))


class Optional(Adapter):
    def __init__(self, expr):
        super(Optional, self).__init__(PpOptional(expr._grammar))


class White(Adapter):
    def __init__(self, ws=" \t\r\n", min=1, max=0, exact=0):
        super(White, self).__init__(PpWhite(ws, min, max, exact))
