class Action:
    @staticmethod
    def action(tokens):
        return tokens


class ExpressionAction(Action):
    @staticmethod
    def action(tokens):
        return {f'${tokens[0].lower()}': tokens[1:]}
