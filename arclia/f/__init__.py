
from typing import Callable, overload, ParamSpec, Protocol, TypeVar


X0 = TypeVar('X0')
X1 = TypeVar('X1')
X2 = TypeVar('X2')
X3 = TypeVar('X3')
X4 = TypeVar('X4')
X5 = TypeVar('X5')
X6 = TypeVar('X6')
X7 = TypeVar('X7')
X8 = TypeVar('X8')
X9 = TypeVar('X9')


@overload
def predecorate(

)-> Callable[[X0], X0]:
    ...


@overload
def predecorate(
    f1: Callable[[X0], X1],
)-> Callable[[X0], X1]:
    ...


@overload
def predecorate(
    f2: Callable[[X1], X2],
    f1: Callable[[X0], X1],
)-> Callable[[X0], X2]:
    ...


@overload
def predecorate(
    f3: Callable[[X2], X3],
    f2: Callable[[X1], X2],
    f1: Callable[[X0], X1],
)-> Callable[[X0], X3]:
    ...


@overload
def predecorate(
    f4: Callable[[X3], X4],
    f3: Callable[[X2], X3],
    f2: Callable[[X1], X2],
    f1: Callable[[X0], X1],
)-> Callable[[X0], X4]:
    ...


@overload
def predecorate(
    f5: Callable[[X4], X5],
    f4: Callable[[X3], X4],
    f3: Callable[[X2], X3],
    f2: Callable[[X1], X2],
    f1: Callable[[X0], X1],
)-> Callable[[X0], X5]:
    ...


@overload
def predecorate(
    f6: Callable[[X5], X6],
    f5: Callable[[X4], X5],
    f4: Callable[[X3], X4],
    f3: Callable[[X2], X3],
    f2: Callable[[X1], X2],
    f1: Callable[[X0], X1],
)-> Callable[[X0], X6]:
    ...


@overload
def predecorate(
    f7: Callable[[X6], X7],
    f6: Callable[[X5], X6],
    f5: Callable[[X4], X5],
    f4: Callable[[X3], X4],
    f3: Callable[[X2], X3],
    f2: Callable[[X1], X2],
    f1: Callable[[X0], X1],
)-> Callable[[X0], X7]:
    ...


@overload
def predecorate(
    f8: Callable[[X7], X8],
    f7: Callable[[X6], X7],
    f6: Callable[[X5], X6],
    f5: Callable[[X4], X5],
    f4: Callable[[X3], X4],
    f3: Callable[[X2], X3],
    f2: Callable[[X1], X2],
    f1: Callable[[X0], X1],
)-> Callable[[X0], X8]:
    ...


@overload
def predecorate(
    f9: Callable[[X8], X9],
    f8: Callable[[X7], X8],
    f7: Callable[[X6], X7],
    f6: Callable[[X5], X6],
    f5: Callable[[X4], X5],
    f4: Callable[[X3], X4],
    f3: Callable[[X2], X3],
    f2: Callable[[X1], X2],
    f1: Callable[[X0], X1],
)-> Callable[[X0], X9]:
    ...


def predecorate(*decorators):
    _decorators = list(reversed(decorators))
    def _decorate(f):
        decorated_f = f
        for d in _decorators:
            decorated_f = d(decorated_f)

        return decorated_f

    return _decorate


def f(x: int):
    return x + 1

def G(_f: Callable[[int], int]):
    def g(x: str):
        return f"Hello {_f(len(x))}"

    return g

def H(_f: Callable[[str], str]):
    def h(x: str):
        return len(_f(x))

    return h

def J(_f: Callable[[int], int]):
    def j(x: int):
        return _f(x) + 1

    return j

Z = predecorate(H, G, J, J, J)

z = Z(f)
