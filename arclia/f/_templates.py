
def _pd_typevars(n: int):
  return f"""
P{n} = ParamSpec('P{n}')
R{n} = TypeVar('R{n}')
  """

def _pd_arg(n: int):
  return f"f{n}: Callable[[Callable[P{n-1}, R{n-1}]], Callable[P{n}, R{n}]]"


def pd(n: int):
  rendered_args = "\n".join(
    f"    {_pd_arg(z)}," for z in reversed(range(1, n + 1))
  )

  return f"""
@overload
def predecorate(
{rendered_args}
)-> Callable[[Callable[P0, R0]], Callable[P{n}, R{n}]]:
    ...
  """
