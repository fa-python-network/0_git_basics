from typing import Tuple

def triangle_area(point_1: Tuple[int, int], point_2: Tuple[int, int], point_3: Tuple[int, int]) -> float:
  return 0.5 * abs((point_2[0] - point_1[0]) * (point_3[1] - point_1[1]) - (point_3[0] - point_1[0]) * (point_2[1] - point_1[1]))

if __name__ == "__main__":
  point_1, point_2, point_3 = (1, 1), (-2, 4), (-2, -2)
  print(f"Test 1: dots {point_1}, {point_2}, {point_3} = {triangle_area(point_1, point_2, point_3)}")
