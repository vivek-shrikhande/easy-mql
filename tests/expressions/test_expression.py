from pyparsing import ParseException
from pytest import raises

from easymql.expressions import Expression as exp


class TestInfixExpression:
    def test_not(self):
        assert exp.parse('NOT true') == {'$not': [True]}
        assert exp.parse('NOT (true)') == {'$not': [True]}
        assert exp.parse('NOT NOT true') == {'$not': [{'$not': [True]}]}

    def test_multiply(self):
        assert exp.parse('1 * 3') == {'$multiply': [1, 3]}
        assert exp.parse('2*3') == {'$multiply': [2, 3]}
        assert exp.parse('1 * 3 * 4') == {'$multiply': [1, 3, 4]}
        with raises(ParseException):
            exp.parse('1 *')
        with raises(ParseException):
            exp.parse('* 3')
        assert exp.parse('1 * (3 * 4)') == {'$multiply': [1, {'$multiply': [3, 4]}]}
        assert exp.parse('1 * -3') == {'$multiply': [1, -3]}
        with raises(ParseException):
            exp.parse('1 * - 3')

    def test_divide(self):
        assert exp.parse('1 / 3') == {'$divide': [1, 3]}
        assert exp.parse('2/3') == {'$divide': [2, 3]}
        assert exp.parse('1 / 3 / 4') == {'$divide': [{'$divide': [1, 3]}, 4]}
        with raises(ParseException):
            exp.parse('1 /')
        with raises(ParseException):
            exp.parse('/ 3')
        assert exp.parse('1 / (3 / 4)') == {'$divide': [1, {'$divide': [3, 4]}]}
        assert exp.parse('1 / -3') == {'$divide': [1, -3]}
        with raises(ParseException):
            exp.parse('1 / - 3')

    def test_mod(self):
        assert exp.parse('1 % 3') == {'$mod': [1, 3]}
        assert exp.parse('2%3') == {'$mod': [2, 3]}
        assert exp.parse('1 % 3 % 4') == {'$mod': [{'$mod': [1, 3]}, 4]}
        with raises(ParseException):
            exp.parse('1 %')
        with raises(ParseException):
            exp.parse('% 3')
        assert exp.parse('1 % (3 % 4)') == {'$mod': [1, {'$mod': [3, 4]}]}
        assert exp.parse('1 % -3') == {'$mod': [1, -3]}
        with raises(ParseException):
            exp.parse('1 % - 3')

    def test_add(self):
        assert exp.parse('1 + 3') == {'$add': [1, 3]}
        assert exp.parse('2+3') == {'$add': [2, 3]}
        assert exp.parse('1 + 3 + 4') == {'$add': [1, 3, 4]}
        with raises(ParseException):
            exp.parse('1 +')
        with raises(ParseException):
            exp.parse('+ 3')
        assert exp.parse('1 + (3 + 4)') == {'$add': [1, {'$add': [3, 4]}]}
        assert exp.parse('1 + -3') == {'$add': [1, -3]}
        assert exp.parse('1 + +3') == {'$add': [1, 3]}
        assert exp.parse('1++3') == {'$add': [1, 3]}
        with raises(ParseException):
            exp.parse('1+++3')
        assert exp.parse('1+(+3)') == {'$add': [1, 3]}
        with raises(ParseException):
            exp.parse('1 + - 3')

    def test_subtract(self):
        assert exp.parse('1 - 3') == {'$subtract': [1, 3]}
        assert exp.parse('2-3') == {'$subtract': [2, 3]}
        assert exp.parse('1 - 3 - 4') == {'$subtract': [{'$subtract': [1, 3]}, 4]}
        with raises(ParseException):
            exp.parse('1 -')
        with raises(ParseException):
            exp.parse('- 3')
        assert exp.parse('1 - (3 - 4)') == {'$subtract': [1, {'$subtract': [3, 4]}]}
        assert exp.parse('1 - -3') == {'$subtract': [1, -3]}
        assert exp.parse('1 - +3') == {'$subtract': [1, 3]}
        assert exp.parse('1--3') == {'$subtract': [1, -3]}
        with raises(ParseException):
            exp.parse('1---3')
        assert exp.parse('1-(-3)') == {'$subtract': [1, -3]}
        with raises(ParseException):
            exp.parse('1 - - 3')

    def test_lt(self):
        assert exp.parse('1 < 3') == {'$lt': [1, 3]}
        assert exp.parse('2<3') == {'$lt': [2, 3]}
        assert exp.parse('1 < 3 < 4') == {'$lt': [{'$lt': [1, 3]}, 4]}
        with raises(ParseException):
            exp.parse('1 <')
        with raises(ParseException):
            exp.parse('< 3')
        assert exp.parse('1 < (3 < 4)') == {'$lt': [1, {'$lt': [3, 4]}]}
        assert exp.parse('1 < -3') == {'$lt': [1, -3]}
        assert exp.parse('1 < +3') == {'$lt': [1, 3]}
        assert exp.parse('1<-3') == {'$lt': [1, -3]}
        with raises(ParseException):
            exp.parse('1<<3')
        assert exp.parse('1<(-3)') == {'$lt': [1, -3]}
        with raises(ParseException):
            exp.parse('1 < - 3')

    def test_lte(self):
        assert exp.parse('1 <= 3') == {'$lte': [1, 3]}
        assert exp.parse('2<=3') == {'$lte': [2, 3]}
        assert exp.parse('1 <= 3 <= 4') == {'$lte': [{'$lte': [1, 3]}, 4]}
        with raises(ParseException):
            exp.parse('1 <=')
        with raises(ParseException):
            exp.parse('<= 3')
        assert exp.parse('1 <= (3 <= 4)') == {'$lte': [1, {'$lte': [3, 4]}]}
        assert exp.parse('1 <= -3') == {'$lte': [1, -3]}
        assert exp.parse('1 <= +3') == {'$lte': [1, 3]}
        assert exp.parse('1<=-3') == {'$lte': [1, -3]}
        with raises(ParseException):
            exp.parse('1 < = 3')
        assert exp.parse('1<=(-3)') == {'$lte': [1, -3]}
        with raises(ParseException):
            exp.parse('1 <= - 3')

    def test_gt(self):
        assert exp.parse('1 > 3') == {'$gt': [1, 3]}
        assert exp.parse('2>3') == {'$gt': [2, 3]}
        assert exp.parse('1 > 3 > 4') == {'$gt': [{'$gt': [1, 3]}, 4]}
        with raises(ParseException):
            exp.parse('1 >')
        with raises(ParseException):
            exp.parse('> 3')
        assert exp.parse('1 > (3 > 4)') == {'$gt': [1, {'$gt': [3, 4]}]}
        assert exp.parse('1 > -3') == {'$gt': [1, -3]}
        assert exp.parse('1 > +3') == {'$gt': [1, 3]}
        assert exp.parse('1>-3') == {'$gt': [1, -3]}
        with raises(ParseException):
            exp.parse('1 > > 3')
        assert exp.parse('1>(-3)') == {'$gt': [1, -3]}
        with raises(ParseException):
            exp.parse('1 > - 3')

    def test_gte(self):
        assert exp.parse('1 >= 3') == {'$gte': [1, 3]}
        assert exp.parse('2>=3') == {'$gte': [2, 3]}
        assert exp.parse('1 >= 3 >= 4') == {'$gte': [{'$gte': [1, 3]}, 4]}
        with raises(ParseException):
            exp.parse('1 >=')
        with raises(ParseException):
            exp.parse('>= 3')
        assert exp.parse('1 >= (3 >= 4)') == {'$gte': [1, {'$gte': [3, 4]}]}
        assert exp.parse('1 >= -3') == {'$gte': [1, -3]}
        assert exp.parse('1 >= +3') == {'$gte': [1, 3]}
        assert exp.parse('1>=-3') == {'$gte': [1, -3]}
        with raises(ParseException):
            exp.parse('1 > = 3')
        assert exp.parse('1>=(-3)') == {'$gte': [1, -3]}
        with raises(ParseException):
            exp.parse('1 >= - 3')

    def test_eq(self):
        assert exp.parse('1 = 3') == {'$eq': [1, 3]}
        assert exp.parse('2=3') == {'$eq': [2, 3]}
        assert exp.parse('1 = 3 = 4') == {'$eq': [{'$eq': [1, 3]}, 4]}
        with raises(ParseException):
            exp.parse('1 =')
        with raises(ParseException):
            exp.parse('= 3')
        assert exp.parse('1 = (3 = 4)') == {'$eq': [1, {'$eq': [3, 4]}]}
        assert exp.parse('1 = -3') == {'$eq': [1, -3]}
        assert exp.parse('1 = +3') == {'$eq': [1, 3]}
        assert exp.parse('1=-3') == {'$eq': [1, -3]}
        with raises(ParseException):
            exp.parse('1 = = 3')
        with raises(ParseException):
            exp.parse('1 == 3')
        assert exp.parse('1=(-3)') == {'$eq': [1, -3]}
        with raises(ParseException):
            exp.parse('1 = - 3')

    def test_ne(self):
        assert exp.parse('1 != 3') == {'$ne': [1, 3]}
        assert exp.parse('2!=3') == {'$ne': [2, 3]}
        assert exp.parse('1 != 3 != 4') == {'$ne': [{'$ne': [1, 3]}, 4]}
        with raises(ParseException):
            exp.parse('1 !=')
        with raises(ParseException):
            exp.parse('!= 3')
        assert exp.parse('1 != (3 != 4)') == {'$ne': [1, {'$ne': [3, 4]}]}
        assert exp.parse('1 != -3') == {'$ne': [1, -3]}
        assert exp.parse('1 != +3') == {'$ne': [1, 3]}
        assert exp.parse('1!=-3') == {'$ne': [1, -3]}
        with raises(ParseException):
            exp.parse('1 != = 3')
        with raises(ParseException):
            exp.parse('1 ! = 3')
        assert exp.parse('1!=(-3)') == {'$ne': [1, -3]}
        with raises(ParseException):
            exp.parse('1 != - 3')

    def test_and(self):
        assert exp.parse('1 AND 3') == {'$and': [1, 3]}
        with raises(ParseException):
            exp.parse('2AND3')
        assert exp.parse('1 AND 3 AND 4') == {'$and': [1, 3, 4]}
        with raises(ParseException):
            exp.parse('1 AND')
        with raises(ParseException):
            exp.parse('AND 3')
        assert exp.parse('1 AND (3 AND 4)') == {'$and': [1, {'$and': [3, 4]}]}
        assert exp.parse('1 AND -3') == {'$and': [1, -3]}
        assert exp.parse('1 AND +3') == {'$and': [1, 3]}
        with raises(ParseException):
            exp.parse('1AND-3')
        with raises(ParseException):
            exp.parse('1 AND = 3')
        assert exp.parse('1 AND (-3)') == {'$and': [1, -3]}
        with raises(ParseException):
            exp.parse('1 AND - 3')

    def test_or(self):
        assert exp.parse('1 OR 3') == {'$or': [1, 3]}
        with raises(ParseException):
            exp.parse('2OR3')
        assert exp.parse('1 OR 3 OR 4') == {'$or': [1, 3, 4]}
        with raises(ParseException):
            exp.parse('1 OR')
        with raises(ParseException):
            exp.parse('OR 3')
        assert exp.parse('1 OR (3 OR 4)') == {'$or': [1, {'$or': [3, 4]}]}
        assert exp.parse('1 OR -3') == {'$or': [1, -3]}
        assert exp.parse('1 OR +3') == {'$or': [1, 3]}
        with raises(ParseException):
            exp.parse('1OR-3')
        with raises(ParseException):
            exp.parse('1 OR = 3')
        assert exp.parse('1 OR (-3)') == {'$or': [1, -3]}
        with raises(ParseException):
            exp.parse('1 OR - 3')

    def test_all(self):
        # should keep adding more
        assert exp.parse('3 < NOT 6 AND 3-2-1') == {
            '$and': [
                {'$lt': [3, {'$not': [6]}]},
                {'$subtract': [{'$subtract': [3, 2]}, 1]},
            ]
        }
        assert exp.parse('6')
