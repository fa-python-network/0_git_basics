def gcf(number_1: int, number_2: int) -> int:
  while number_1 > 0 and number_2 > 0:
    if number_1 > number_2:
      number_1, number_2 = number_1 % number_2, number_2
    else:
      number_1, number_2 = number_1, number_2 % number_1    
  return max(number_1, number_2)

if __name__ == "__main__":
  number_1, number_2 = 10, 36
  print(f"Test 1: GCF({number_1}, {number_2}) = {gcf(number_1, number_2)}")

  number_1, number_2 = 765, 27
  print(f"Test 2: GCF({number_1}, {number_2}) = {gcf(number_1, number_2)}")
