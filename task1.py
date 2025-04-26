file_name = "sample.txt"

try:
  f = open(file_name)
  print("Reading file content:")
  count = 0
  for x in f:
    count += 1
    print(f"Line {count}: {x}");
except:
  print(f"Error: The file '{file_name}' was not found.")