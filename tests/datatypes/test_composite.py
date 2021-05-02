from pyparsing import ParseException
from pytest import raises

from easymql.expressions import Expression
from easymql.datatypes.primary import Boolean, Decimal, Integer, Null, String


class TestCompositeDataType:
    def test_array(self):
        array = Expression
        assert array.parse('[]') == []
        assert array.parse('[[], 0]') == [[], Integer(0)]
        assert array.parse('[{"a": "b"}]') == [{"a": String("b")}]
        assert array.parse('[{"a": []}]') == [{"a": []}]
        assert array.parse('[1,2,3, null, [[]], [1.2], {}, {"a": []}]') == [
            Integer(1),
            Integer(2),
            Integer(3),
            Null(None),
            [[]],
            [Decimal(1.2)],
            {},
            {"a": []},
        ]
        # array with expressions
        assert array.parse('[a+b, c+d, CONCAT("hello", " ", "world!")]') == [
            {'$add': ['$a', '$b']},
            {'$add': ['$c', '$d']},
            {'$concat': ['hello', ' ', 'world!']},
        ]

    def test_object(self):
        obj = Expression
        assert obj.parse('{}') == {}
        assert obj.parse('{"size": 1024}') == {'size': Integer(1024)}
        with raises(ParseException):
            assert obj.parse("{'size': 1024}") == {'size': Integer(1024)}
        with raises(ParseException):
            assert obj.parse('{size: 1024}') == {'size': Integer(1024)}
        assert obj.parse('{"nested": {"empty": {}}}') == {'nested': {'empty': {}}}
        assert obj.parse(
            '{"int": 1, "float": 1.3, "bool": true, "null": null, "string": "hello", '
            '"array": [1, {}], "object": {"array": []}}'
        ) == {
            'int': Integer(1),
            'float': Decimal(1.3),
            'bool': Boolean(True),
            'null': Null(None),
            'string': String('hello'),
            'array': [Integer(1), {}],
            'object': {'array': []},
        }
        # object with expressions
        assert obj.parse(
            '''
            {
                "day": EXTRACT(DAY_OF_YEAR, date),
                "year": EXTRACT(YEAR, date)
            }
            '''
        ) == {
            'day': {'$dayOfYear': {'date': '$date'}},
            'year': {'$year': {'date': '$date'}},
        }
