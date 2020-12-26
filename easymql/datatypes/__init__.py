from easymql import Grammar
from easymql.datatypes.composite import Array, Object
from easymql.datatypes.primary import Boolean, Null, Number, String
from easymql.proxies import data_type_proxy


class DataType(Grammar):

    grammar = data_type_proxy
    grammar <<= Array() | Object() | Number() | String() | Boolean() | Null()
