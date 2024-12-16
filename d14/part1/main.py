import re

map_x, map_y = 101, 103

def main():
  with open("input.txt", "r") as file:
    guards = []
    for line in file:
      guards.append([int(s) for s in re.findall(r"p=(\d+),(\d+) v=(-?\d+),(-?\d+)", line)[0]])

  quadrans = {(True, True): 0, (True, False): 0, (False, True): 0, (False, False): 0}

  for g in guards:
    g[0] = (g[0] + 100 * g[2]) % map_x
    g[1] = (g[1] + 100 * g[3]) % map_y

    if g[0] != map_x // 2  and g[1] != map_y // 2:
      quadrans[(g[0] > map_x // 2, g[1] > map_y // 2)] += 1

  result = 1
  for q in quadrans:
    result *= quadrans[q]
  print(result)
  

if __name__ == "__main__":
  main()