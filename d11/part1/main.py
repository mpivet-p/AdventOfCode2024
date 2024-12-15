memory = {}
# With memory dict and 25 blinks: 5805 calls to expand()
# -> [0.02s user 0.01s system 90% cpu 0.033 total]
# Without: 553995
# -> [0.21s user 0.01s system 90% cpu 0.245 total]

def expand(stone, times):
  strstone = str(stone)
  stones = []

  if times == 0:
    return 1
  if (stone, times) in memory:
    return memory[(stone, times)]

  if stone == 0:
    stones.append(1)
  elif (len(strstone) % 2) == 0:
    stones.append(int(strstone[len(strstone) // 2:]))
    stones.append(int(strstone[:len(strstone) // 2]))
  else:
    stones.append(stone * 2024)

  result = sum(expand(st, times - 1) for st in stones)

  memory[(stone, times)] = result
  return result

def main():
  with open("input.txt", "r") as file:
    stones = [int(c) for c in file.read().split()]

  result = sum(expand(st, 75) for st in stones)
  print(result)

if __name__ == "__main__":
  main()