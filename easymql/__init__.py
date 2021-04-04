class MetaGrammar(type):
    def __init__(cls, name, bases, dct):
        super(MetaGrammar, cls).__init__(name, bases, dct)
        try:
            cls._set_parse_action(cls.action)
        except AttributeError as e:
            pass

    def __add__(cls, other):
        return cls.grammar.__add__(other)

    def __and__(cls, other):
        return cls.grammar.__and__(other)

    # def __eq__(cls, other):
    #     return cls.grammar.__eq__(other)

    def __getitem__(cls, key):
        return cls.grammar[key]

    def __mul__(cls, other):
        return cls.grammar.__mul__(other)

    # def __ne__(cls, other):
    #     return cls.grammar.__ne__(other)

    def __or__(cls, other):
        return cls.grammar.__or__(other)

    def __radd__(cls, other):
        return cls.grammar.__radd__(other)

    def __rand__(cls, other):
        return cls.grammar.__rand__(other)

    def __repr__(cls):
        return f'<{cls.__name__}>'

    def __req__(cls, other):
        return cls.grammar.__req__(other)

    def __rmul__(cls, other):
        return cls.grammar.__rmul__(other)

    def __rne__(cls, other):
        return cls.grammar.__rne__(other)

    def __ror__(cls, other):
        return cls.grammar.__ror__(other)

    def __rsub__(cls, other):
        return cls.grammar.__rsub__(other)

    def __rxor__(cls, other):
        return cls.grammar.__rxor__(other)

    def __str__(cls):
        return cls.__name__

    def __sub__(cls, other):
        return cls.grammar.__sub__(other)

    def __xor__(cls, other):
        return cls.grammar.__xor__(other)

    @property
    def _grammar(cls):
        return cls.grammar._grammar


class Grammar(metaclass=MetaGrammar):
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"{self.__class__.__name__}({repr(self.value)})"

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.value == other.value

    def __ne__(self, other):
        return not self == other

    @classmethod
    def parse(cls, string, explode=True):
        return cls.grammar.parse(string, explode)

    @classmethod
    def _set_parse_action(cls, action):
        try:
            cls.grammar._set_parse_action(action)
        except AttributeError:
            pass

    @classmethod
    def _set_name(cls, name):
        try:
            cls.grammar._set_name(name)
        except AttributeError:
            pass


class Adapter:
    def __init__(self, grammar):
        self.grammar = grammar
        try:
            self._set_parse_action(self.action)
        except AttributeError as e:
            pass

    def _set_parse_action(self, action):
        try:
            self.grammar.setParseAction(action)
        except AttributeError as e:
            pass

    def _set_name(self, name):
        try:
            self.grammar.setName(name)
        except AttributeError as e:
            pass

    def __add__(self, other):
        return Adapter(self.grammar.__add__(other._grammar))

    def __and__(self, other):
        return Adapter(self.grammar.__and__(other._grammar))

    def __eq__(self, other):
        return Adapter(self.grammar.__eq__(other._grammar))

    def __getitem__(self, key):
        return Adapter(self.grammar[key])

    def __mul__(self, other):
        return Adapter(self.grammar.__mul__(other._grammar))

    def __ne__(self, other):
        return Adapter(self.grammar.__ne__(other._grammar))

    def __or__(self, other):
        return Adapter(self.grammar.__or__(other._grammar))

    def __radd__(self, other):
        return Adapter(self.grammar.__radd__(other._grammar))

    def __rand__(self, other):
        return Adapter(self.grammar.__rand__(other._grammar))

    # def __repr__(self):
    #     return f'{self.__class__.__name__}({self.value})'

    def __req__(self, other):
        return Adapter(self.grammar.__req__(other._grammar))

    def __rmul__(self, other):
        return Adapter(self.grammar.__rmul__(other._grammar))

    def __rne__(self, other):
        return Adapter(self.grammar.__rne__(other._grammar))

    def __ror__(self, other):
        return Adapter(self.grammar.__ror__(other._grammar))

    def __rsub__(self, other):
        return Adapter(self.grammar.__rsub__(other._grammar))

    def __rxor__(self, other):
        return Adapter(self.grammar.__rxor__(other._grammar))

    # def __str__(self):
    #     return self.__class__.__name__

    def __sub__(self, other):
        return Adapter(self.grammar.__sub__(other._grammar))

    def __xor__(self, other):
        return Adapter(self.grammar.__xor__(other._grammar))

    @property
    def _grammar(self):
        return self.grammar

    def parse(self, string, explode=True):
        result = self.grammar.parseString(string, parseAll=True).asList()
        if explode and len(result) == 1:
            return result.pop()
        else:
            return result
