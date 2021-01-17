from pyparsing import ParseException
from pytest import raises

from easymql.expressions import Expression


class TestMiscellaneousExpression:
    @classmethod
    def setup_class(cls):
        cls.exp = Expression()

    def test_random(self):
        assert self.exp.parse('RANDOM()') == [{'$rand': {}}]

    def test_sample_rate(self):
        assert self.exp.parse('SAMPLE_RATE(0.33)') == [{'$sampleRate': [0.33]}]
        with raises(ParseException):
            self.exp.parse('SAMPLE_RATE()')
