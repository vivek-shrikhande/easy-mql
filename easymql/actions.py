class Action:
    @staticmethod
    def action(tokens):
        return tokens


class ExpressionAction(Action):
    @staticmethod
    def action(tokens):
        tokens = tokens.asList()
        name = tokens.pop(0)
        return {f'${name.lower()}': tokens[0] if len(tokens) == 1 else tokens}
