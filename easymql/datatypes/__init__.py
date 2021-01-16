from easymql import Grammar
from easymql.datatypes.composite import Array, Object
from easymql.datatypes.primary import Boolean, Date, Null, Number, String
from easymql.proxies import data_type_proxy


class DataType(Grammar):

    grammar = data_type_proxy
    grammar <<= Array() | Boolean() | Date() | Object() | Number() | String() | Null()
