from easymql.meta import Grammar
from easymql.keywords import (
    SYS_CLUSTER_TIME,
    SYS_CURRENT,
    SYS_DESCEND,
    SYS_KEEP,
    SYS_NOW,
    SYS_PRUNE,
    SYS_REMOVE,
    SYS_ROOT,
)


class SystemVariables(Grammar):

    grammar = (
        SYS_CLUSTER_TIME
        | SYS_CURRENT
        | SYS_DESCEND
        | SYS_KEEP
        | SYS_NOW
        | SYS_PRUNE
        | SYS_REMOVE
        | SYS_ROOT
    )

    @classmethod
    def action(cls, token):
        return '$' + token[0]
