from easymql import Grammar
from easymql.datatypes import DataType
from easymql.expressions.arithmetic import ArithmeticExpression
from easymql.expressions.boolean import BooleanExpression
from easymql.expressions.conditional import ConditionalExpression
from easymql.expressions.set import SetExpression
from easymql.expressions.trigonometry import TrigonometryExpression
from easymql.proxies import expression_proxy


class Expression(Grammar):

    grammar = expression_proxy
    grammar <<= (
        ArithmeticExpression()
        | BooleanExpression()
        | ConditionalExpression()
        | SetExpression()
        | TrigonometryExpression()
        | DataType()
    )
