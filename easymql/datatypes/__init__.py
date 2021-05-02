from easymql import Grammar
from easymql.datatypes.composite import Array, Object
from easymql.datatypes.primary import Boolean, Date, Null, Number, String


class DataType(Grammar):

    grammar = Array | Boolean | Date | Object | Number | String | Null
