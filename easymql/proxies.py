from itertools import starmap, repeat

from pyparsing import Forward


(data_type_proxy, expression_proxy) = starmap(Forward, repeat((), 2))
