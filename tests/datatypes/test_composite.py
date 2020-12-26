from pyparsing import ParseException
from pytest import raises

from easymql.datatypes import DataType


class TestCompositeDataType:
    def test_array(self):
        array = DataType()
        assert array.parse('[]') == [[]]
        assert array.parse('[[], 0]') == [[[], 0]]
        assert array.parse('[{"a": "b"}]') == [[{"a": "b"}]]
        assert array.parse('[{"a": []}]') == [[{"a": []}]]
        assert array.parse('[1,2,3, null, [[]], [1.2], {}, {"a": []}]') == [
            [1, 2, 3, None, [[]], [1.2], {}, {"a": []}]
        ]

    def test_object(self):
        obj = DataType()
        assert obj.parse('{}') == [{}]
        assert obj.parse('{"size": 1024}') == [{'size': 1024}]
        with raises(ParseException):
            assert obj.parse("{'size': 1024}") == [{'size': 1024}]
        with raises(ParseException):
            assert obj.parse('{size: 1024}') == [{'size': 1024}]
        assert obj.parse('{"nested": {"empty": {}}}') == [{'nested': {'empty': {}}}]
        assert obj.parse(
            '{"int": 1, "float": 1.3, "bool": true, "null": null, "string": "hello", '
            '"array": [1, {}], "object": {"array": []}}'
        ) == [
            {
                'int': 1,
                'float': 1.3,
                'bool': True,
                'null': None,
                'string': 'hello',
                'array': [1, {}],
                'object': {'array': []},
            }
        ]
