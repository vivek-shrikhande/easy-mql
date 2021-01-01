from easymql import Grammar
from easymql.datatypes import DataType
from easymql.expressions.arithmetic import ArithmeticExpression
from easymql.proxies import expression_proxy


class Expression(Grammar):

    grammar = expression_proxy
    grammar <<= ArithmeticExpression() | DataType()
