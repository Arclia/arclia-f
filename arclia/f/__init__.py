
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
X10 = TypeVar('X10')

@overload
def prewrap(

)-> Callable[[X0], X0]:
    ...
  
@overload
def prewrap(
    f1: Callable[[X0], X1],
)-> Callable[[X0], X1]:
    ...
  
@overload
def prewrap(
    f2: Callable[[X1], X2],
    f1: Callable[[X0], X1],
)-> Callable[[X0], X2]:
    ...
  
@overload
def prewrap(
    f3: Callable[[X2], X3],
    f2: Callable[[X1], X2],
    f1: Callable[[X0], X1],
)-> Callable[[X0], X3]:
    ...
  
@overload
def prewrap(
    f4: Callable[[X3], X4],
    f3: Callable[[X2], X3],
    f2: Callable[[X1], X2],
    f1: Callable[[X0], X1],
)-> Callable[[X0], X4]:
    ...
  
@overload
def prewrap(
    f5: Callable[[X4], X5],
    f4: Callable[[X3], X4],
    f3: Callable[[X2], X3],
    f2: Callable[[X1], X2],
    f1: Callable[[X0], X1],
)-> Callable[[X0], X5]:
    ...
  
@overload
def prewrap(
    f6: Callable[[X5], X6],
    f5: Callable[[X4], X5],
    f4: Callable[[X3], X4],
    f3: Callable[[X2], X3],
    f2: Callable[[X1], X2],
    f1: Callable[[X0], X1],
)-> Callable[[X0], X6]:
    ...
  
@overload
def prewrap(
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
def prewrap(
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
def prewrap(
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
  
@overload
def prewrap(
    f10: Callable[[X9], X10],
    f9: Callable[[X8], X9],
    f8: Callable[[X7], X8],
    f7: Callable[[X6], X7],
    f6: Callable[[X5], X6],
    f5: Callable[[X4], X5],
    f4: Callable[[X3], X4],
    f3: Callable[[X2], X3],
    f2: Callable[[X1], X2],
    f1: Callable[[X0], X1],
)-> Callable[[X0], X10]:
    ...


def prewrap(*wrappers: Callable):
    _wrappers = list(reversed(wrappers))
    def _wrap(f):
        wrapped_f = f
        for w in _wrappers:
            wrapped_f = w(wrapped_f)

        return wrapped_f

    return _wrap


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

Z = prewrap(H, G, J, J, J)

z = Z(f)
