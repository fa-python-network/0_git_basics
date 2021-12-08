import os

def open_file_is_available(file_name: str) -> str:
  file_path = os.path.join(os.curdir, file_name)
  if os.path.isfile(file_path):
    with open(file_path) as f:
      return f.read()
  return f"404. File {file_name} not found"

if __name__ == "__main__":
  print(f"Test 1: file lorenipsum.txt    {open_file_is_available('lorenipsum.txt')}")
  print(f"Test 2: file notexist.txt    {open_file_is_available('notexist.txt')}")
