from pyparsing import ParseException, alphas
from pytest import raises

from easymql.core import Word
from easymql.utils import delimited_list, keyword_group


class TestDelimitedList:
    def test_min_0_max_0(self):
        dlist = delimited_list(Word(alphas), min=0, max=0)
        assert dlist.parse('') == []
        with raises(ParseException):
            assert dlist.parse('a') == 'a'

    def test_min_0_max_2(self):
        dlist = delimited_list(Word(alphas), min=0, max=2)
        assert dlist.parse('') == []
        assert dlist.parse('a') == 'a'
        assert dlist.parse('a, b') == ['a', 'b']
        with raises(ParseException):
            assert dlist.parse('a, b, c') == [
                'a',
                'b',
                'c',
            ]

    def test_min_2_max_4(self):
        dlist = delimited_list(Word(alphas), min=2, max=4)
        with raises(ParseException):
            assert dlist.parse('') == []
        with raises(ParseException):
            assert dlist.parse('a') == 'a'
        assert dlist.parse('a, b') == ['a', 'b']
        assert dlist.parse('a, b, c') == ['a', 'b', 'c']
        assert dlist.parse('a, b, c, d') == ['a', 'b', 'c', 'd']
        with raises(ParseException):
            assert dlist.parse('a, b, c, d, e') == [
                'a',
                'b',
                'c',
                'd',
                'e',
            ]

    def test_min_2_max_ellipsis(self):
        dlist = delimited_list(Word(alphas), min=2)
        with raises(ParseException):
            assert dlist.parse('') == []
        with raises(ParseException):
            assert dlist.parse('a') == 'a'
        assert dlist.parse('a, b') == ['a', 'b']
        assert dlist.parse('a, b, c') == ['a', 'b', 'c']
        assert dlist.parse('a, b, c, d') == ['a', 'b', 'c', 'd']
        assert dlist.parse('a, b, c, d, e') == [
            'a',
            'b',
            'c',
            'd',
            'e',
        ]

    def test_min_1_max_1(self):
        dlist = delimited_list(Word(alphas), min=1, max=1)
        with raises(ParseException):
            assert dlist.parse('') == []
        assert dlist.parse('a') == 'a'
        with raises(ParseException):
            assert dlist.parse('a, b') == ['a', 'b']
        with raises(ParseException):
            assert dlist.parse('a, b, c') == [
                'a',
                'b',
                'c',
            ]

    def test_min_1_max_ellipses(self):
        dlist = delimited_list(Word(alphas), min=1)
        with raises(ParseException):
            assert dlist.parse('') == []
        assert dlist.parse('a') == 'a'
        assert dlist.parse('a, b') == ['a', 'b']
        assert dlist.parse('a, b, c') == [
            'a',
            'b',
            'c',
        ]

    def test_min_2_max_2(self):
        dlist = delimited_list(Word(alphas), min=2, max=2)
        with raises(ParseException):
            assert dlist.parse('') == []
        with raises(ParseException):
            assert dlist.parse('a') == 'a'
        assert dlist.parse('a, b') == ['a', 'b']
        with raises(ParseException):
            assert dlist.parse('a, b, c') == [
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
            assert dlist.parse('') == []
        with raises(ParseException):
            assert dlist.parse('a') == 'a'
        assert dlist.parse('a, b') == ['a', 'b']
        assert dlist.parse('a, b, c') == ['a', 'b', 'c']


# class TestKeywordGroup:
def test_keyword_group():
    assert keyword_group('AS').parse('AS') == 'AS'
    with raises(ParseException):
        keyword_group('ASON').parse('AS ON')
    assert keyword_group('AS ON').parse('AS ON') == ['AS', 'ON']
    assert keyword_group('AS     ON').parse('AS ON') == ['AS', 'ON']
    assert keyword_group('AS ON').parse('AS     ON') == ['AS', 'ON']
    assert keyword_group('AS ON').parse('AS     ON') == ['AS', 'ON']
    assert (
        keyword_group(
            '''AS
    ON'''
        ).parse('AS     ON')
        == ['AS', 'ON']
    )
