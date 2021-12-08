import copy
from typing import List

def get_average_element(values_list: List[float]) -> float:
  if len(values_list) % 2 == 0 or len(values_list) == 0:
    raise ValueError("incorrect values list")
  new_values_list = copy.copy(values_list)
  for i in range(len(new_values_list)):
    for j in range(len(new_values_list)):
      if new_values_list[i] > new_values_list[j]:
        new_values_list[i], new_values_list[j] = new_values_list[j], new_values_list[i]
  n = (len(new_values_list) - 1) // 2
  return new_values_list[n]

list_1 = [3, 2, 7, 1, 6, 4, 5]
print(f"Test 1: list with numbers 1..7, average value {get_average_element(list_1)}")

list_2 = [3, 2, 7, 1, 6, 4, 5, 8] # should raise error
print(f"Test 1: list with numbers 1..8, average value {get_average_element(list_2)}")
