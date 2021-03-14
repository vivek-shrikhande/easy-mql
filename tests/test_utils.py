from pyparsing import alphas, ParseException, Word
from pytest import raises

from easymql.utils import delimited_list


class TestDelimitedList:
    def test_min_0_max_0(self):
        dlist = delimited_list(Word(alphas), min=0, max=0)
        assert dlist.parseString('').asList() == []
        with raises(ParseException):
            assert dlist.parseString('a', parseAll=True).asList() == ['a']

    def test_min_0_max_2(self):
        dlist = delimited_list(Word(alphas), min=0, max=2)
        assert dlist.parseString('').asList() == []
        assert dlist.parseString('a').asList() == ['a']
        assert dlist.parseString('a, b').asList() == ['a', 'b']
        with raises(ParseException):
            assert dlist.parseString('a, b, c', parseAll=True).asList() == [
                'a',
                'b',
                'c',
            ]

    def test_min_2_max_4(self):
        dlist = delimited_list(Word(alphas), min=2, max=4)
        with raises(ParseException):
            assert dlist.parseString('', parseAll=True).asList() == []
        with raises(ParseException):
            assert dlist.parseString('a', parseAll=True).asList() == ['a']
        assert dlist.parseString('a, b').asList() == ['a', 'b']
        assert dlist.parseString('a, b, c').asList() == ['a', 'b', 'c']
        assert dlist.parseString('a, b, c, d').asList() == ['a', 'b', 'c', 'd']
        with raises(ParseException):
            assert dlist.parseString('a, b, c, d, e', parseAll=True).asList() == [
                'a',
                'b',
                'c',
                'd',
                'e',
            ]

    def test_min_2_max_ellipsis(self):
        dlist = delimited_list(Word(alphas), min=2)
        with raises(ParseException):
            assert dlist.parseString('', parseAll=True).asList() == []
        with raises(ParseException):
            assert dlist.parseString('a', parseAll=True).asList() == ['a']
        assert dlist.parseString('a, b').asList() == ['a', 'b']
        assert dlist.parseString('a, b, c').asList() == ['a', 'b', 'c']
        assert dlist.parseString('a, b, c, d').asList() == ['a', 'b', 'c', 'd']
        assert dlist.parseString('a, b, c, d, e', parseAll=True).asList() == [
            'a',
            'b',
            'c',
            'd',
            'e',
        ]

    def test_min_1_max_1(self):
        dlist = delimited_list(Word(alphas), min=1, max=1)
        with raises(ParseException):
            assert dlist.parseString('', parseAll=True).asList() == []
        assert dlist.parseString('a', parseAll=True).asList() == ['a']
        with raises(ParseException):
            assert dlist.parseString('a, b', parseAll=True).asList() == ['a', 'b']
        with raises(ParseException):
            assert dlist.parseString('a, b, c', parseAll=True).asList() == [
                'a',
                'b',
                'c',
            ]

    def test_min_2_max_2(self):
        dlist = delimited_list(Word(alphas), min=2, max=2)
        with raises(ParseException):
            assert dlist.parseString('', parseAll=True).asList() == []
        with raises(ParseException):
            assert dlist.parseString('a', parseAll=True).asList() == ['a']
        assert dlist.parseString('a, b').asList() == ['a', 'b']
        with raises(ParseException):
            assert dlist.parseString('a, b, c', parseAll=True).asList() == [
                'a',
                'b',
                'c',
            ]

    def test_min_ellipsis(self):
        with raises(ValueError):
            delimited_list(Word(alphas), min=...)

    def test_default(self):
        dlist = delimited_list(Word(alphas))
        with raises(ParseException):
            assert dlist.parseString('', parseAll=True).asList() == []
        with raises(ParseException):
            assert dlist.parseString('a', parseAll=True).asList() == ['a']
        assert dlist.parseString('a, b').asList() == ['a', 'b']
        assert dlist.parseString('a, b, c', parseAll=True).asList() == ['a', 'b', 'c']
