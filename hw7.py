from typing import List

def multiply(*args: List[int]) -> int:
  if len(args) == 0:
    return None
  result = 1
  for value in args:
    if type(value) is not int:
      raise ValueError(f"{value} is not a number")
    result *= value
  return result

if __name__ == "__main__":
  numbers = [1, 2, 3, 4, 5]
  print(f"Test 1: multiply {numbers} = {multiply(*numbers)}")

  not_numbers = [1, 2, "x", 4, 5]
  print(f"Test 2: multiply {not_numbers} = {multiply(*not_numbers)}")
