import random

def generate_test_file(filename, number_of_lines):
  with open(filename, "w") as f:
    for i in range(number_of_lines):
      code_snippet = ""
      for j in range(random.randint(1, 100)):
        code_snippet += random.choice("abcdefghijklmnopqrstuvwxyz0123456789")
      f.write(code_snippet + "\n")

if __name__ == "__main__":
  filename = "test.txt"
  number_of_lines = 100
  generate_test_file(filename, number_of_lines)
