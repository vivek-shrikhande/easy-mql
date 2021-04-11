from pyparsing import ParseException
from pytest import raises

from easymql.expressions import Expression


class TestStringsExpression:
    @classmethod
    def setup_class(cls):
        cls.exp = Expression

    def test_concat(self):
        assert self.exp.parse('CONCAT("Hello", "easy", "mql!")') == {
            '$concat': ['Hello', 'easy', 'mql!']
        }
        with raises(ParseException):
            self.exp.parse('CONCAT("Hello")')

    def test_index_of_bytes(self):
        assert self.exp.parse('INDEX_OF_BYTES("foo.bar.fi", ".")') == {
            '$indexOfBytes': ['foo.bar.fi', '.']
        }
        assert self.exp.parse('INDEX_OF_BYTES("foo.bar.fi", ".", 5)') == {
            '$indexOfBytes': ['foo.bar.fi', '.', 5]
        }
        assert self.exp.parse('INDEX_OF_BYTES("vanilla", "ll", 0, 2)') == {
            '$indexOfBytes': ['vanilla', 'll', 0, 2]
        }
        with raises(ParseException):
            self.exp.parse('INDEX_OF_BYTES("vanilla")')
        with raises(ParseException):
            self.exp.parse('INDEX_OF_BYTES("vanilla", "ll", 0, 2, 1)')

    def test_index_of_cp(self):
        assert self.exp.parse('INDEX_OF_CP("foo.bar.fi", ".")') == {
            '$indexOfCP': ['foo.bar.fi', '.']
        }
        assert self.exp.parse('INDEX_OF_CP("foo.bar.fi", ".", 5)') == {
            '$indexOfCP': ['foo.bar.fi', '.', 5]
        }
        assert self.exp.parse('INDEX_OF_CP("vanilla", "ll", 0, 2)') == {
            '$indexOfCP': ['vanilla', 'll', 0, 2]
        }
        with raises(ParseException):
            self.exp.parse('INDEX_OF_CP("vanilla")')
        with raises(ParseException):
            self.exp.parse('INDEX_OF_CP("vanilla", "ll", 0, 2, 1)')

    def test_trim(self):
        assert self.exp.parse('TRIM(" ggoodbyeee ")') == {
            '$trim': {'input': ' ggoodbyeee '}
        }
        assert self.exp.parse('TRIM(" ggoodbyeee ", "ge")') == {
            '$trim': {'input': ' ggoodbyeee ', 'chars': 'ge'}
        }
        assert self.exp.parse('TRIM(" ggoodbyeee ", " gd")') == {
            '$trim': {'input': ' ggoodbyeee ', 'chars': ' gd'}
        }
        with raises(ParseException):
            self.exp.parse('TRIM(" ggoodbyeee ", " gd", "ee")')

    def test_ltrim(self):
        assert self.exp.parse('LTRIM(" ggoodbyeee ")') == {
            '$ltrim': {'input': ' ggoodbyeee '}
        }
        assert self.exp.parse('LTRIM(" ggoodbyeee ", "ge")') == {
            '$ltrim': {'input': ' ggoodbyeee ', 'chars': 'ge'}
        }
        assert self.exp.parse('LTRIM(" ggoodbyeee ", " gd")') == {
            '$ltrim': {'input': ' ggoodbyeee ', 'chars': ' gd'}
        }
        with raises(ParseException):
            self.exp.parse('LTRIM(" ggoodbyeee ", " gd", "ee")')

    def test_rtrim(self):
        assert self.exp.parse('RTRIM(" ggoodbyeee ")') == {
            '$rtrim': {'input': ' ggoodbyeee '}
        }
        assert self.exp.parse('RTRIM(" ggoodbyeee ", "ge")') == {
            '$rtrim': {'input': ' ggoodbyeee ', 'chars': 'ge'}
        }
        assert self.exp.parse('RTRIM(" ggoodbyeee ", " gd")') == {
            '$rtrim': {'input': ' ggoodbyeee ', 'chars': ' gd'}
        }
        with raises(ParseException):
            self.exp.parse('RTRIM(" ggoodbyeee ", " gd", "ee")')

    def test_regex_find(self):
        assert self.exp.parse('REGEX_FIND("Easymql", "ql")') == {
            '$regexFind': {'input': 'Easymql', 'regex': 'ql'}
        }
        assert self.exp.parse('REGEX_FIND("Easymql", "ql", "i")') == {
            '$regexFind': {'input': 'Easymql', 'regex': 'ql', 'options': 'i'}
        }
        with raises(ParseException):
            self.exp.parse('REGEX_FIND("Easymql")')
        with raises(ParseException):
            self.exp.parse('REGEX_FIND("Easymql", "ql", "i", "test")')

    def test_regex_find_all(self):
        assert self.exp.parse('REGEX_FIND_ALL("Easymql", "ql")') == {
            '$regexFindAll': {'input': 'Easymql', 'regex': 'ql'}
        }
        assert self.exp.parse('REGEX_FIND_ALL("Easymql", "ql", "i")') == {
            '$regexFindAll': {'input': 'Easymql', 'regex': 'ql', 'options': 'i'}
        }
        with raises(ParseException):
            self.exp.parse('REGEX_FIND_ALL("Easymql")')
        with raises(ParseException):
            self.exp.parse('REGEX_FIND_ALL("Easymql", "ql", "i", "test")')

    def test_regex_match(self):
        assert self.exp.parse('REGEX_MATCH("Easymql", "ql")') == {
            '$regexMatch': {'input': 'Easymql', 'regex': 'ql'}
        }
        assert self.exp.parse('REGEX_MATCH("Easymql", "ql", "i")') == {
            '$regexMatch': {'input': 'Easymql', 'regex': 'ql', 'options': 'i'}
        }
        with raises(ParseException):
            self.exp.parse('REGEX_MATCH("Easymql")')
        with raises(ParseException):
            self.exp.parse('REGEX_MATCH("Easymql", "ql", "i", "test")')

    def test_replace(self):
        assert self.exp.parse('REPLACE("Easymql", "Easy", "easy")') == {
            '$replaceOne': {'input': 'Easymql', 'find': 'Easy', 'replacement': 'easy'}
        }
        with raises(ParseException):
            self.exp.parse('REPLACE("Easymql")')
        with raises(ParseException):
            self.exp.parse('REPLACE("Easymql", "Easy")')
        with raises(ParseException):
            self.exp.parse('REPLACE("Easymql", "Easy", "easy", "1")')

    def test_replace_all(self):
        assert self.exp.parse('REPLACE_ALL("Easymql= Easymql", "Easy", "easy")') == {
            '$replaceAll': {
                'input': 'Easymql= Easymql',
                'find': 'Easy',
                'replacement': 'easy',
            }
        }
        with raises(ParseException):
            self.exp.parse('REPLACE_ALL("Easymql= Easymql")')
        with raises(ParseException):
            self.exp.parse('REPLACE_ALL("Easymql= Easymql", "Easy")')
        with raises(ParseException):
            self.exp.parse('REPLACE_ALL("Easymql= Easymql", "Easy", "easy", "1")')

    def test_split(self):
        assert self.exp.parse('SPLIT("June-15-2013", "-")') == {
            '$split': ['June-15-2013', '-']
        }
        with raises(ParseException):
            self.exp.parse('SPLIT("June-15-2013")')
        with raises(ParseException):
            self.exp.parse('SPLIT("June-15-2013", "-", "1")')

    def test_string_lenght(self):
        assert self.exp.parse('STR_LEN_BYTES("abcde")') == {'$strLenBytes': 'abcde'}
        with raises(ParseException):
            self.exp.parse('STR_LEN_BYTES("abcd", "efgh")')

    def test_string_lenght_cp(self):
        assert self.exp.parse('STR_LEN_CP("Easy mql")') == {'$strLenCP': 'Easy mql'}
        with raises(ParseException):
            self.exp.parse('STR_LEN_CP("abcd", "efgh")')

    def test_string_case_comparison(self):
        assert self.exp.parse('STRCASECMP("Easy", "easy")') == {
            '$strcasecmp': ['Easy', 'easy']
        }
        with raises(ParseException):
            self.exp.parse('STRCASECMP("Easy")')
        with raises(ParseException):
            self.exp.parse('STRCASECMP("Easy", "easy", "mql")')

    def test_substr(self):
        assert self.exp.parse('SUBSTR("easymql", 0, 2)') == {
            '$substr': ['easymql', 0, 2]
        }
        with raises(ParseException):
            self.exp.parse('SUBSTR("easymql")')
        with raises(ParseException):
            self.exp.parse('SUBSTR("easymql", 0)')
        with raises(ParseException):
            self.exp.parse('SUBSTR("easymql", 0, 2, 2)')

    def test_substr_bytes(self):
        assert self.exp.parse('SUBSTR_BYTES("easymql", 0, 2)') == {
            '$substrBytes': ['easymql', 0, 2]
        }
        with raises(ParseException):
            self.exp.parse('SUBSTR_BYTES("easymql")')
        with raises(ParseException):
            self.exp.parse('SUBSTR_BYTES("easymql", 0)')
        with raises(ParseException):
            self.exp.parse('SUBSTR_BYTES("easymql", 0, 2, 2)')

    def test_substr_cp(self):
        assert self.exp.parse('SUBSTR_CP("easymql", 0, 2)') == {
            '$substrCP': ['easymql', 0, 2]
        }
        with raises(ParseException):
            self.exp.parse('SUBSTR_CP("easymql")')
        with raises(ParseException):
            self.exp.parse('SUBSTR_CP("easymql", 0)')
        with raises(ParseException):
            self.exp.parse('SUBSTR_CP("easymql", 0, 2, 2)')

    def test_to_lower(self):
        assert self.exp.parse('TO_LOWER("EASYMQL")') == {'$toLower': ['EASYMQL']}
        with raises(ParseException):
            self.exp.parse('TO_LOWER("EASY", "MQL")')

    def test_to_upper(self):
        assert self.exp.parse('TO_UPPER("easymql")') == {'$toUpper': ['easymql']}
        with raises(ParseException):
            self.exp.parse('TO_LOWER("easy", "mql")')
