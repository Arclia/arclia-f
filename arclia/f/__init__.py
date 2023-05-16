
from typing import Callable, overload, ParamSpec, Protocol, TypeVar


P0 = ParamSpec('P0')
R0 = TypeVar('R0')

P1 = ParamSpec('P1')
R1 = TypeVar('R1')

P2 = ParamSpec('P2')
R2 = TypeVar('R2')

P3 = ParamSpec('P3')
R3 = TypeVar('R3')

P4 = ParamSpec('P4')
R4 = TypeVar('R4')

P5 = ParamSpec('P5')
R5 = TypeVar('R5')

P6 = ParamSpec('P6')
R6 = TypeVar('R6')

P7 = ParamSpec('P7')
R7 = TypeVar('R7')

P8 = ParamSpec('P8')
R8 = TypeVar('R8')

P9 = ParamSpec('P9')
R9 = TypeVar('R9')


@overload
def predecorate()-> Callable[[Callable[P0, R0]], Callable[P0, R0]]:
    ...


@overload
def predecorate(
    f1: Callable[[Callable[P0, R0]], Callable[P1, R1]],
)-> Callable[[Callable[P0, R0]], Callable[P1, R1]]:
    ...


@overload
def predecorate(
    f2: Callable[[Callable[P1, R1]], Callable[P2, R2]],
    f1: Callable[[Callable[P0, R0]], Callable[P1, R1]],
)-> Callable[[Callable[P0, R0]], Callable[P2, R2]]:
    ...


@overload
def predecorate(
    f3: Callable[[Callable[P2, R2]], Callable[P3, R3]],
    f2: Callable[[Callable[P1, R1]], Callable[P2, R2]],
    f1: Callable[[Callable[P0, R0]], Callable[P1, R1]],
)-> Callable[[Callable[P0, R0]], Callable[P3, R3]]:
    ...


@overload
def predecorate(
    f4: Callable[[Callable[P3, R3]], Callable[P4, R4]],
    f3: Callable[[Callable[P2, R2]], Callable[P3, R3]],
    f2: Callable[[Callable[P1, R1]], Callable[P2, R2]],
    f1: Callable[[Callable[P0, R0]], Callable[P1, R1]],
)-> Callable[[Callable[P0, R0]], Callable[P4, R4]]:
    ...


@overload
def predecorate(
    f5: Callable[[Callable[P4, R4]], Callable[P5, R5]],
    f4: Callable[[Callable[P3, R3]], Callable[P4, R4]],
    f3: Callable[[Callable[P2, R2]], Callable[P3, R3]],
    f2: Callable[[Callable[P1, R1]], Callable[P2, R2]],
    f1: Callable[[Callable[P0, R0]], Callable[P1, R1]],
)-> Callable[[Callable[P0, R0]], Callable[P5, R5]]:
    ...


@overload
def predecorate(
    f6: Callable[[Callable[P5, R5]], Callable[P6, R6]],
    f5: Callable[[Callable[P4, R4]], Callable[P5, R5]],
    f4: Callable[[Callable[P3, R3]], Callable[P4, R4]],
    f3: Callable[[Callable[P2, R2]], Callable[P3, R3]],
    f2: Callable[[Callable[P1, R1]], Callable[P2, R2]],
    f1: Callable[[Callable[P0, R0]], Callable[P1, R1]],
)-> Callable[[Callable[P0, R0]], Callable[P6, R6]]:
    ...


@overload
def predecorate(
    f7: Callable[[Callable[P6, R6]], Callable[P7, R7]],
    f6: Callable[[Callable[P5, R5]], Callable[P6, R6]],
    f5: Callable[[Callable[P4, R4]], Callable[P5, R5]],
    f4: Callable[[Callable[P3, R3]], Callable[P4, R4]],
    f3: Callable[[Callable[P2, R2]], Callable[P3, R3]],
    f2: Callable[[Callable[P1, R1]], Callable[P2, R2]],
    f1: Callable[[Callable[P0, R0]], Callable[P1, R1]],
)-> Callable[[Callable[P0, R0]], Callable[P7, R7]]:
    ...


@overload
def predecorate(
    f8: Callable[[Callable[P7, R7]], Callable[P8, R8]],
    f7: Callable[[Callable[P6, R6]], Callable[P7, R7]],
    f6: Callable[[Callable[P5, R5]], Callable[P6, R6]],
    f5: Callable[[Callable[P4, R4]], Callable[P5, R5]],
    f4: Callable[[Callable[P3, R3]], Callable[P4, R4]],
    f3: Callable[[Callable[P2, R2]], Callable[P3, R3]],
    f2: Callable[[Callable[P1, R1]], Callable[P2, R2]],
    f1: Callable[[Callable[P0, R0]], Callable[P1, R1]],
)-> Callable[[Callable[P0, R0]], Callable[P8, R8]]:
    ...


@overload
def predecorate(
    f9: Callable[[Callable[P8, R8]], Callable[P9, R9]],
    f8: Callable[[Callable[P7, R7]], Callable[P8, R8]],
    f7: Callable[[Callable[P6, R6]], Callable[P7, R7]],
    f6: Callable[[Callable[P5, R5]], Callable[P6, R6]],
    f5: Callable[[Callable[P4, R4]], Callable[P5, R5]],
    f4: Callable[[Callable[P3, R3]], Callable[P4, R4]],
    f3: Callable[[Callable[P2, R2]], Callable[P3, R3]],
    f2: Callable[[Callable[P1, R1]], Callable[P2, R2]],
    f1: Callable[[Callable[P0, R0]], Callable[P1, R1]],
)-> Callable[[Callable[P0, R0]], Callable[P9, R9]]:
    ...


def predecorate(*decorators):
    _decorators = list(reversed(decorators))
    def _decorate(f: Callable[P0, R0]):
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
