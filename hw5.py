import math
from typing import Callable

def f(x: float) -> float:
  return (6-x) * math.sin(x / 6) 

def drange(x: float, y: float, h: float):
  while x < y:
    yield float(x)
    x += h

def max_of_f(f: Callable, a: int = 0, b: int = 1, h: float = 0.1) -> float:
  max_value = f(a)
  for i in drange(a, b, h):
    max_value = max(max_value, f(i))
  return max_value

if __name__ == "__main__":
  print(f"Test 1: max value of (6-x)sin(x/6) on range [0, 12] is {max_of_f(f, 0, 12)}")
