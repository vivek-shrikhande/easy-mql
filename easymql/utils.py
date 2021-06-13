from easymql.core import (
    Suppress,
    Empty,
    Literal,
    Keyword,
    And,
    ParseExpression,
    Adapter,
)


class DelimitedList(Adapter):
    def __init__(self, expr, delimiter=Literal(','), min=2, max=...):
        self.expr = expr
        super(DelimitedList, self).__init__(
            self._delimited_list(expr, delimiter, min, max)._grammar
        )

    def _delimited_list(self, expr, delimiter=Literal(','), min=2, max=...):
        if min is Ellipsis:
            raise ValueError('Min value should be definite. Use 0 instead.')
        if min == 0:
            if max == 0:
                return Empty()
            elif max == 1:
                return expr[0, 1]
            elif max is Ellipsis:
                return (expr + (Suppress(delimiter) + expr)[0, max])[0, 1]
            else:
                return (expr + (Suppress(delimiter) + expr)[0, max - 1])[0, 1]
        else:
            if max == 1:
                return expr
            elif max is Ellipsis:
                return expr + (Suppress(delimiter) + expr)[min - 1, max]
            else:
                return expr + (Suppress(delimiter) + expr)[min - 1, max - 1]

    def __str__(self):
        if isinstance(self.expr.get_adapter_grammar(), ParseExpression):
            return f'{{ {self.expr._grammar} }}...'
        else:
            return f'{self.expr._grammar}...'


def safe_cast_int(int_str):
    try:
        return int(int_str)
    except Exception:
        return int_str


def keyword_group(keyword_string):
    return And(map(Keyword, keyword_string.split()))
