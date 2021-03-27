from pyparsing import ParseException
from pytest import raises

from easymql.expressions import Expression


class TestObjectExpression:
    @classmethod
    def setup_class(cls):
        cls.exp = Expression

    def test_merge_object(self):
        assert self.exp.parse('MERGE_OBJECTS({"a": 1}, null)') == {
            '$mergeObjects': [{'a': 1}, None]
        }
        assert self.exp.parse(
            'MERGE_OBJECTS({"a": 1}, {"a": 2, "b": 2}, {"a": 3, "c": 3})'
        ) == {'$mergeObjects': [{'a': 1}, {'a': 2, 'b': 2}, {'a': 3, 'c': 3}]}
        with raises(ParseException):
            self.exp.parse('MERGE_OBJECTS({"a": 1})')

    def test_object_to_array(self):
        assert self.exp.parse('OBJECT_TO_ARRAY({"item": "foo", "qty": 25})') == {
            '$objectToArray': {'item': 'foo', 'qty': 25}
        }
        with raises(ParseException):
            self.exp.parse('OBJECT_TO_ARRAY({"item": "foo", "qty": 25}, {"a": 1})')
        with raises(ParseException):
            self.exp.parse('OBJECT_TO_ARRAY()')
