from pyparsing import ParseException
from pytest import raises

from easymql.expressions import Expression


class TestArrayExpression:
    @classmethod
    def setup_class(cls):
        cls.exp = Expression

    def test_array_elem_at(self):
        assert self.exp.parse('ARRAY_ELEM_AT( [ 1, 2, 3 ], 0 )') == {
            '$arrayElemAt': [[1, 2, 3], 0]
        }
        assert self.exp.parse('ARRAY_ELEM_AT( "$favorites", 0 )') == {
            '$arrayElemAt': ["$favorites", 0]
        }
        with raises(ParseException):
            self.exp.parse('ARRAY_ELEM_AT()')

    def test_array_to_object(self):
        assert self.exp.parse(
            'ARRAY_TO_OBJECT([{ "k": "item", "v": "abc123"}, { "k": "qty", "v": 25 } ] )'
        ) == {'$arrayToObject': [[{"k": "item", "v": "abc123"}, {"k": "qty", "v": 25}]]}
        assert self.exp.parse(
            'ARRAY_TO_OBJECT([[ "item", "abc123"], [ "qty", 25 ] ])'
        ) == {'$arrayToObject': [[["item", "abc123"], ["qty", 25]]]}
        with raises(ParseException):
            self.exp.parse('ARRAY_TO_OBJECT()')

    def test_concat_arrays(self):
        assert self.exp.parse('CONCAT_ARRAYS( [ "hello", " "], [ "world" ] )') == {
            '$concatArrays': [['hello', ' '], ['world']]
        }
        assert self.exp.parse('CONCAT_ARRAYS( "array_name1", "array_name2" )') == {
            '$concatArrays': ["array_name1", "array_name2"]
        }
        with raises(ParseException):
            self.exp.parse('CONCAT_ARRAYS()')

    def test_filter(self):
        assert self.exp.parse('FILTER("items", "item", "price")') == {
            '$filter': {'input': 'items', 'as': 'item', 'cond': 'price'}
        }
        with raises(ParseException):
            self.exp.parse('FILTER()')

    def test_first(self):
        assert self.exp.parse('FIRST("price")') == {'$first': ['price']}
        with raises(ParseException):
            self.exp.parse('FIRST()')

    def test_in(self):
        assert self.exp.parse('IN(2, [ 1, 2, 3 ])') == {'$in': [2, [1, 2, 3]]}
        assert self.exp.parse('IN("abc", [ "xyz", "abc" ])') == {
            '$in': ['abc', ['xyz', 'abc']]
        }
        with raises(ParseException):
            self.exp.parse('IN()')

    def test_index_of_array(self):
        assert self.exp.parse('INDEX_OF_ARRAY([ "a", "abc" ], "a")') == {
            '$indexOfArray': [['a', 'abc'], 'a']
        }
        assert self.exp.parse('INDEX_OF_ARRAY("array_name", "a")') == {
            '$indexOfArray': ['array_name', 'a']
        }
        with raises(ParseException):
            self.exp.parse('INDEX_OF_ARRAY()')

    def test_is_array(self):
        assert self.exp.parse('IS_ARRAY([ "hello", "world" ])') == {
            '$isArray': [['hello', 'world']]
        }
        assert self.exp.parse('IS_ARRAY("array_name")') == {'$isArray': ['array_name']}
        with raises(ParseException):
            self.exp.parse('IS_ARRAY()')

    def test_last(self):
        assert self.exp.parse('LAST("price")') == {'$last': ['price']}
        with raises(ParseException):
            self.exp.parse('LAST()')

    def test_map(self):
        assert self.exp.parse('MAP("items", "item", "price")') == {
            '$map': {'input': 'items', 'as': 'item', 'in': 'price'}
        }
        with raises(ParseException):
            self.exp.parse('MAP()')

    def test_object_to_array(self):
        assert self.exp.parse('OBJECT_TO_ARRAY({"item": "foo", "qty": 25})') == {
            '$objectToArray': {'item': 'foo', 'qty': 25}
        }
        assert self.exp.parse('OBJECT_TO_ARRAY("dimensions")') == {
            '$objectToArray': 'dimensions'
        }
        assert self.exp.parse('OBJECT_TO_ARRAY("object_name")') == {
            '$objectToArray': 'object_name'
        }
        with raises(ParseException):
            self.exp.parse('OBJECT_TO_ARRAY()')

    def test_range(self):
        assert self.exp.parse('RANGE(0, "distance", 25)') == {
            '$range': [0, 'distance', 25]
        }
        with raises(ParseException):
            self.exp.parse('RANGE()')

    def test_reduce(self):
        assert self.exp.parse('REDUCE( ["a", "b", "c"], "", ["value", "this"] )') == {
            '$reduce': {
                'input': ['a', 'b', 'c'],
                'initialValue': '',
                'in': ['value', 'this'],
            }
        }
        assert self.exp.parse(
            'REDUCE( "probabilityArr", 1, MULTIPLY("value", "this" ))'
        ) == {
            '$reduce': {
                'input': 'probabilityArr',
                'initialValue': 1,
                'in': {'$multiply': ['value', 'this']},
            }
        }
        with raises(ParseException):
            self.exp.parse('REDUCE()')

    def test_reverse_array(self):
        assert self.exp.parse('REVERSE_ARRAY("favorites")') == {
            '$reverseArray': ["favorites"]
        }
        assert self.exp.parse('REVERSE_ARRAY([1, 2, 3])') == {
            '$reverseArray': [[1, 2, 3]]
        }
        with raises(ParseException):
            self.exp.parse('REVERSE_ARRAY()')

    def test_size(self):
        assert self.exp.parse('SIZE("colors")') == {'$size': ["colors"]}
        with raises(ParseException):
            self.exp.parse('SIZE()')

    def test_slice(self):
        assert self.exp.parse('SLICE("favorites", 3)') == {'$slice': ["favorites", 3]}
        assert self.exp.parse('SLICE("favorites", 12, -2)') == {
            '$slice': ["favorites", 12, -2]
        }
        with raises(ParseException):
            self.exp.parse('SLICE()')

    def test_zip(self):
        assert self.exp.parse('ZIP( [[1], [2, 3], [4]], true, [ "a", "b", "c" ] )') == {
            '$zip': {
                'inputs': [[1], [2, 3], [4]],
                'useLongestLength': True,
                'defaults': ["a", "b", "c"],
            }
        }
        assert self.exp.parse('ZIP( [[1], [2, 3]], true )') == {
            '$zip': {'inputs': [[1], [2, 3]], 'useLongestLength': True}
        }

        with raises(ParseException):
            self.exp.parse('ZIP()')
