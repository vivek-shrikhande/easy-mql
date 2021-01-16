from pyparsing import ParserElement


class Grammar(ParserElement):
    def __new__(cls, *args, **kwargs):
        if 'grammar' not in cls.__dict__:
            raise AttributeError('Grammar not specified')
        return super().__new__(cls, *args, **kwargs)

    def __init__(self):
        super().__init__()
        self.name = self.__class__.__name__
        try:
            self.setParseAction(self.action)
        except AttributeError:
            pass

    def parseImpl(self, input_string, loc, do_actions=True):
        return self.__class__.grammar.parseImpl(input_string, loc, do_actions)

    def parse(self, input_string):
        return super().parseString(input_string, parseAll=True).asList()
