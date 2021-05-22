from pyparsing import ParseException
from pytest import raises

from easymql.expressions import Expression as Exp


def test_system_variables():
    assert Exp.parse('$CLUSTER_TIME') == '$$CLUSTER_TIME'
    assert Exp.parse('$CURRENT') == '$$CURRENT'
    assert Exp.parse('$DESCEND') == '$$DESCEND'
    assert Exp.parse('$KEEP') == '$$KEEP'
    assert Exp.parse('$NOW') == '$$NOW'
    assert Exp.parse('$PRUNE') == '$$PRUNE'
    assert Exp.parse('$REMOVE') == '$$REMOVE'
    assert Exp.parse('$ROOT') == '$$ROOT'

    # lower case & others
    for value in (
        '$cluster_time',
        '$current',
        '$descend',
        '$keep',
        '$now',
        '$prune',
        '$remove',
        '$root',
        '$REMOVE$ROOT',
        '$$ROOT',
    ):
        with raises(ParseException):
            Exp.parse(value)
