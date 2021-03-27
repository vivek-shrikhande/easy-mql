from pyparsing import ParseException
from pytest import raises

from easymql.expressions.others import FieldPath


class TestOthers:
    def test_FieldPath(self):
        assert FieldPath.parse("'hello'") == '$hello'
        assert FieldPath.parse("'newline\ntest'") == '$newline\ntest'
        assert FieldPath.parse("'hello \\'world\\''") == "$hello 'world'"
        assert FieldPath.parse('\'hello "world"\'') == '$hello "world"'
        assert FieldPath.parse("'unicode \u1F600 test'") == "$unicode \u1F600 test"
        assert (
            FieldPath.parse(
                """'multi
line'"""
            )
            == "$multi\nline"
        )
        with raises(ParseException):
            assert FieldPath.parse('"hello"') == "$hello"

