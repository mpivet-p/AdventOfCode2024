import sys

sys.setrecursionlimit(3000)

possible = {}
absent = set()

def makeable(towels, to_make):
  count = 0
  if to_make in possible:
    return possible["to_make"]

  if to_make in towels:
    count += 1

  for i in range(len(to_make) - 1, 0, -1):
    if to_make[:i] in towels and to_make[i:] not in absent:
      if to_make[i:] in possible:
        count += possible[to_make[i:]]
        continue

      result = makeable(towels, to_make[i:])
      if result > 0:
        count += result
      else:
        absent.add(to_make[i:])

  possible[to_make] = count
  return count

def main():
  to_make = []
  with open("input.txt", "r") as file:
    i = 0
    lines = file.read().split("\n")
    available_towels = set(lines[0].strip().split(", "))
    to_make = lines[2:]

  result = 0
  for tm in to_make:
    result += makeable(available_towels, tm)

  print(result)

if __name__ == "__main__":
  main()