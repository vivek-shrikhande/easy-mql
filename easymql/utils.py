from pyparsing import Suppress, Empty


def delimited_list(expr, delimiter=',', min=2, max=...):
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


def mongo_expression(name, tokens):
    return {f'${name}': tokens[0] if len(tokens) == 1 else tokens.asList()}
