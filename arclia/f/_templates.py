
from io import StringIO

def _pd_typevars(n: int):
  return f"""
X{n} = TypeVar('X{n}')
  """

def _pd_arg(n: int):
  return f"f{n}: Callable[[X{n - 1}], X{n}]"


def pd(n: int):
  rendered_args = "\n".join(
    f"    {_pd_arg(z)}," for z in reversed(range(1, n + 1))
  )

  return f"""
@overload
def predecorate(
{rendered_args}
)-> Callable[[X0], X{n}]:
    ...
  """

def boom(n: int):
  w = StringIO()

  for x in range(0, n + 1):
    w.write(_pd_typevars(x))

  for x in range(0, n + 1):
    w.write(pd(x))

  return w.getvalue()
