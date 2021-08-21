from pyparsing import ParseException
from pytest import raises

from easymql.expressions import Expression


class TestSetExpression:
    @classmethod
    def setup_class(cls):
        cls.exp = Expression

    def test_all_elements_true(self):
        assert self.exp.parse('ALL([ true, 1, "someString", false])') == {
            '$allElementsTrue': [[True, 1, 'someString', False]]
        }

        with raises(ParseException):
            self.exp.parse('ALL()')

    def test_any_element_true(self):
        assert self.exp.parse('ANY([ true, 1, "someString", false])') == {
            '$anyElementTrue': [[True, 1, 'someString', False]]
        }

        with raises(ParseException):
            self.exp.parse('ANY()')

    def test_set_difference(self):
        assert self.exp.parse('SET_DIFFERENCE( [ "a", "b", "a" ], [ "b", "a" ] )') == {
            '$setDifference': [['a', 'b', 'a'], ['b', 'a']]
        }

        with raises(ParseException):
            self.exp.parse('SET_DIFFERENCE(1.2)')
        with raises(ParseException):
            self.exp.parse('SET_DIFFERENCE()')

    def test_set_equals(self):
        assert self.exp.parse('SET_EQUALS( [ "a", "b", "a" ], [ "b", "a" ] )') == {
            '$setEquals': [['a', 'b', 'a'], ['b', 'a']]
        }

        with raises(ParseException):
            self.exp.parse('SET_EQUALS(1.2)')
        with raises(ParseException):
            self.exp.parse('SET_EQUALS()')

    def test_set_intersection(self):
        assert self.exp.parse(
            'SET_INTERSECTION( [ "a", "b", "a" ], [ "b", "a" ] )'
        ) == {'$setIntersection': [["a", "b", "a"], ["b", "a"]]}
        with raises(ParseException):
            self.exp.parse('SET_INTERSECTION(1.2)')
        with raises(ParseException):
            self.exp.parse('SET_INTERSECTION()')

    def test_set_is_subset(self):
        assert self.exp.parse('SET_IS_SUBSET( ["a", "b", "a"], ["b", "a"] )') == {
            '$setIsSubset': [['a', 'b', 'a'], ['b', 'a']]
        }

        with raises(ParseException):
            self.exp.parse('SET_IS_SUBSET(1.2)')
        with raises(ParseException):
            self.exp.parse('SET_IS_SUBSET()')

    def test_set_union(self):
        assert self.exp.parse('SET_UNION( ["a", "b", "a"], ["b", "a"] )') == {
            '$setUnion': [['a', 'b', 'a'], ['b', 'a']]
        }

        with raises(ParseException):
            self.exp.parse('SET_UNION(1.2)')
        with raises(ParseException):
            self.exp.parse('SET_UNION()')
