from pyparsing import ParseException
from pytest import raises

from easymql.groupacc import GroupByAccumulatorExpression


class TestGroupByAccumulatorsExpression:
    @classmethod
    def setup_class(cls):
        cls.exp = GroupByAccumulatorExpression

    def test_add_to_set(self):
        assert self.exp.parse('ADD_TO_SET("price")') == {"$addToSet": ["price"]}
        with raises(ParseException):
            self.exp.parse("ADD_TO_SET()")

    def test_avg(self):
        assert self.exp.parse('AVG("price")') == {"$avg": ["price"]}
        with raises(ParseException):
            self.exp.parse("AVG()")

    def test_first(self):
        assert self.exp.parse('FIRST("price")') == {'$first': ['price']}
        with raises(ParseException):
            self.exp.parse('FIRST()')

    def test_last(self):
        assert self.exp.parse('LAST("price")') == {'$last': ['price']}
        with raises(ParseException):
            self.exp.parse('LAST()')

    def test_max(self):
        assert self.exp.parse('MAX("price")') == {"$max": ["price"]}
        assert self.exp.parse('MAX("price")') == {"$max": ["price"]}
        with raises(ParseException):
            self.exp.parse("MAX()")

    def test_merge_object(self):
        assert self.exp.parse('MERGE_OBJECTS({"a": 1})') == {
            '$mergeObjects': [{'a': 1}]
        }
        with raises(ParseException):
            self.exp.parse('MERGE_OBJECTS({"a": 1}, null)')
        with raises(ParseException):
            self.exp.parse(
                'MERGE_OBJECTS({"a": 1}, {"a": 2, "b": 2}, {"a": 3, "c": 3})'
            )

    def test_min(self):
        assert self.exp.parse('MIN("price")') == {"$min": ["price"]}
        with raises(ParseException):
            self.exp.parse("AVG()")

    def test_push(self):
        assert self.exp.parse('PUSH("price")') == {"$push": ["price"]}
        with raises(ParseException):
            self.exp.parse("PUSH()")

    def test_std_pev_pop(self):
        assert self.exp.parse('STD_DEV_POP("price")') == {"$stdDevPop": ["price"]}
        with raises(ParseException):
            self.exp.parse("STD_DEV_POP()")

    def test_std_dev_samp(self):
        assert self.exp.parse('STD_DEV_SAMP("price")') == {"$stdDevSamp": ["price"]}
        with raises(ParseException):
            self.exp.parse("STD_DEV_SAMP()")

    def test_sum(self):
        assert self.exp.parse('SUM("price")') == {"$sum": ["price"]}
        with raises(ParseException):
            self.exp.parse("SUM()")
