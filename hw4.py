import math
from typing import List, Union

def solve_quadratic_equation(*args: List) -> Union[List[int], None]:
  if len(args) == 3:
    a, b, c = args
    d = b * b - 4 * a * c
    if d < 0:
      return []
    x1, x2 = (-1 * b - math.sqrt(d)) / (2 * a), (-1 * b + math.sqrt(d)) / (2 * a)
    if x1 == x2:
      return [x1]
    else:
      return [x1, x2]
  elif len(args) == 2:
    b, c = args
    x = (-1 * c) / b
    return [x]
  elif len(args) == 1:
    if args[0] == 0:
      return ["*"]
    else:
      return []
  else:
    return None

if __name__ == "__main__":
  a, b, c = 3, -14, -5
  print(f"Test 1: {a}*x^2 + {b}*x + {c} = 0, x = {solve_quadratic_equation(a, b, c)}")

  a, b, c = 1, 4, 16
  print(f"Test 2: {a}*x^2 + {b}*x + {c} = 0, x = {solve_quadratic_equation(a, b, c)}")

  a, b, c = 1, -8, 16
  print(f"Test 3: {a}*x^2 + {b}*x + {c} = 0, x = {solve_quadratic_equation(a, b, c)}")

  b, c = 5, 10
  print(f"Test 4: {b}*x + {c} = 0, x = {solve_quadratic_equation(b, c)}")

  c = 0
  print(f"Test 5: {c} = 0, x = {solve_quadratic_equation(c)}")

  c = 1
  print(f"Test 6: {c} = 0, x = {solve_quadratic_equation(c)}")

  a, b, c, d, e = 1, 2, 3, 4, 5
  print(f"Test 7: Input {a} {b} {c} {d} {e} = 0, x = {solve_quadratic_equation(a, b, c, d, e)}")


  print(f"Test 8: No input, x = {solve_quadratic_equation()}")
