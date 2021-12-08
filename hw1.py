import logging
from typing import Optional

def operation_on_two_numbers(number_1: int, number_2: int, operation: str) -> Optional[int]:
  if operation == '+':
    return number_1 + number_2
  elif operation == '-':
    return number_1 - number_2
  elif operation == '*':
    return number_1 * number_2
  elif operation == '/':
    return number_1 / number_2
  else:
    logging.error("Неизвестная операция")
    return None

if __name__ == "__main__":
  number_1, number_2 = 3, 5
  print(f"Test 1: {number_1} + {number_2} = {operation_on_two_numbers(number_1, number_2, '+')}")
  print(f"Test 2: {number_1} - {number_2} = {operation_on_two_numbers(number_1, number_2, '-')}")
  print(f"Test 3: {number_1} * {number_2} = {operation_on_two_numbers(number_1, number_2, '*')}")
  print(f"Test 4: {number_1} / {number_2} = {operation_on_two_numbers(number_1, number_2, '/')}")
  print(f"Test 5: {number_1} ^ {number_2} = {operation_on_two_numbers(number_1, number_2, '^')}")
