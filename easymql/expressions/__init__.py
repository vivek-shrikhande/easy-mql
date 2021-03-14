from easymql import Grammar
from easymql.datatypes import DataType
from easymql.expressions.arithmetic import ArithmeticExpression
from easymql.expressions.boolean import BooleanExpression
from easymql.expressions.conditional import ConditionalExpression
from easymql.expressions.datasize import DataSizeExpression
from easymql.expressions.set import SetExpression
from easymql.expressions.trigonometry import TrigonometryExpression
from easymql.expressions.type import TypeExpression
from easymql.proxies import expression_proxy
from easymql.expressions.miscellaneous import MiscellaneousExpression


class Expression(Grammar):

    grammar = expression_proxy
    grammar <<= (
        ArithmeticExpression
        | BooleanExpression
        | ConditionalExpression
        | DataSizeExpression
        | MiscellaneousExpression
        | SetExpression
        | TrigonometryExpression
        | TypeExpression
        | DataType
    )
