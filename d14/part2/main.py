import re
import time

map_x, map_y = 101, 103

def display_map(guards, secs):
  print(f"============================================[ {secs + 1: 3} Elapsed ]============================================")

  s = ""
  for i in range(map_y):
    for j in range(map_y):
      count = sum([1 if g[0] == j and g[1] == i else 0 for g in guards])
      if count > 0:
        s += "█"
      else:
        s += " "
    s += "\n"

  print(s)

def main():
  with open("input.txt", "r") as file:
    guards = []
    for line in file:
      guards.append([int(s) for s in re.findall(r"p=(\d+),(\d+) v=(-?\d+),(-?\d+)", line)[0]])

  quadrans = {(True, True): 0, (True, False): 0, (False, True): 0, (False, False): 0}

  for i in range(10000):
    for g in guards:
      g[0] = (g[0] + g[2]) % map_x
      g[1] = (g[1] + g[3]) % map_y

    if i % map_y == 51: # When the "Pattern" seems to appear
      display_map(guards, i)

if __name__ == "__main__":
  main()