import math
from core.primitives import Constant
from operations.arithmetic import Log, Exp

e = Constant(math.e)
pi = Constant(math.pi)


def log(argument):

    return Log(argument)


def exp(argument):

    return Exp(argument)