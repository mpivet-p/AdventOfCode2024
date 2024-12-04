import re

def main():
  # example = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

  with open("input.txt", "r") as file:
    example = file.read()

  # Split on the do() and then ignore everything after the dont()
  example = "".join([t.partition("don't()")[0] for t in example.split("do()")])

  reg_result = re.findall(r'mul\((\d+),(\d+)\)', example)

  result = 0

  for r in reg_result:
    result += int(r[0]) * int(r[1])
  print(result)

if __name__ == "__main__":
  main()


  