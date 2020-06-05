from multimethod import multimethod


# Different methods are used depending on the type of input parameter
@multimethod(int, int)
def foo(a, b):
    return a + b


@multimethod(float, float)
def foo(a, b):
    return a - b


@multimethod(str, str)
def foo(a, b):
    return a + b


@multimethod(str)
@multimethod(str, int)
def foo(a, b=10):
    c = str(b)
    return a + c


@multimethod(float)
@multimethod(float, int)
@multimethod(float, int, int)
def foo(a, b=10, c=10):
    return a + b + c
