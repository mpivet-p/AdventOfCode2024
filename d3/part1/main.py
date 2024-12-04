import re

def main():
  # example = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"

  with open("input.txt", "r") as file:
    example = file.read()

  reg_result = re.findall(r'mul\((\d+),(\d+)\)', example)

  result = 0

  for r in reg_result:
    result += int(r[0]) * int(r[1])
  print(result)

if __name__ == "__main__":
  main()