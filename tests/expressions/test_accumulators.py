from pyparsing import ParseException
from pytest import raises

from easymql.expressions import Expression


class TestAccumulatorsExpression:
    @classmethod
    def setup_class(cls):
        cls.exp = Expression

    def test_avg(self):
        assert self.exp.parse('AVG("price", "quantity")') == {
            "$avg": ["price", "quantity"]
        }
        with raises(ParseException):
            self.exp.parse("AVG()")

    def test_max(self):
        assert self.exp.parse('MAX("price", "quantity")') == {
            "$max": ["price", "quantity"]
        }
        assert self.exp.parse('MAX("price")') == {"$max": ["price"]}
        with raises(ParseException):
            self.exp.parse("MAX()")

    def test_min(self):
        assert self.exp.parse('MIN("price", "quantity")') == {
            "$min": ["price", "quantity"]
        }
        with raises(ParseException):
            self.exp.parse("AVG()")

    def test_std_pev_pop(self):
        assert self.exp.parse('STD_DEV_POP("price", "quantity")') == {
            "$stdDevPop": ["price", "quantity"]
        }
        with raises(ParseException):
            self.exp.parse("STD_DEV_POP()")

    def test_std_dev_samp(self):
        assert self.exp.parse('STD_DEV_SAMP("price", "quantity")') == {
            "$stdDevSamp": ["price", "quantity"]
        }
        with raises(ParseException):
            self.exp.parse("STD_DEV_SAMP()")

    def test_sum(self):
        assert self.exp.parse('SUM("price", "quantity")') == {
            "$sum": ["price", "quantity"]
        }
        with raises(ParseException):
            self.exp.parse("SUM()")
