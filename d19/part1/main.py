import sys

sys.setrecursionlimit(3000)

possible = set()
absent = set()

def makeable(towels, to_make):

  for i in range(len(to_make) - 1, 0, -1):
    if to_make[:i] in towels:
      # print(f"[{to_make}] '{to_make[:i]}' `{to_make[i:]}`")

      if to_make[i:] in towels:
        return True
      elif to_make[i:] not in absent and makeable(towels, to_make[i:]):
        return True
      else:
        absent.add(to_make[i:])

  return False

def main():
  to_make = []
  with open("input.txt", "r") as file:
    i = 0
    lines = file.read().split("\n")
    available_towels = set(lines[0].strip().split(", "))
    to_make = lines[2:]

  result = 0
  for tm in to_make:
    if makeable(available_towels, tm):
      result += 1

  print(result)

if __name__ == "__main__":
  main()