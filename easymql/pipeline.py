from easymql.core import HashComment
from easymql.stages import Stages


Pipeline = Stages[1, ...]
Pipeline.ignore(HashComment())
