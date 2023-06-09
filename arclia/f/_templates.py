
from io import StringIO

def _prewrap_typevars(n: int):
  return f"X{n} = TypeVar('X{n}')"

def _prewrap_arg(n: int):
  return f"f{n}: Callable[[X{n - 1}], X{n}]"


def generate_prewrap_overload(n: int):
  rendered_args = "\n".join(
    f"    {_prewrap_arg(z)}," for z in reversed(range(1, n + 1))
  )

  return f"""
@overload
def prewrap(
{rendered_args}
)-> Callable[[X0], X{n}]:
    ...
  """

def boom(n: int):
  w = StringIO()

  for x in range(0, n + 1):
    w.write(_prewrap_typevars(x))
    w.write("\n")

  for x in range(0, n + 1):
    w.write(generate_prewrap_overload(x))

  return w.getvalue()
