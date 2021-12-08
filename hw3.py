from typing import Tuple, Union

def gcf(number_1: int, number_2: int) -> int:
  while number_1 > 0 and number_2 > 0:
    if number_1 > number_2:
      number_1, number_2 = number_1 % number_2, number_2
    else:
      number_1, number_2 = number_1, number_2 % number_1    
  return max(number_1, number_2)

def reduce_fraction(*args) -> Union[Tuple[int, int], None]:
  if len(args) == 0:
    return None
  if type(args[0]) is int:
    numerator, denominator = args[0], args[1]
    fraction_gcf = gcf(numerator, denominator)
    return int(numerator / fraction_gcf), int(denominator / fraction_gcf)
  elif type(args[0]) is list:
    fraction_gcf = gcf(args[0][0], args[0][1])
    args[0][0], args[0][1] = int(args[0][0] / fraction_gcf), int(args[0][1] / fraction_gcf)

if __name__ == "__main__":
  numerator, denominator = 10, 36
  print(f"Test 1: reduce_fraction({numerator}, {denominator}) = {reduce_fraction(numerator, denominator)}")

  fraction_list = [765, 135]
  reduce_fraction(fraction_list)
  print(f"Test 2: reduce_fraction([765, 135]) = {fraction_list}")
