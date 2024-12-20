import numpy as np
import sys

costs = {}
solutions = []

def solve(map, pos, visited):
  if map[tuple(pos)] == "E":
    solutions.append(visited)
    return True
  
  solved = False

  next_pos = [(0, 1), (1, 0), (0, -1), (-1, 0)] + pos
  for nc in next_pos:
    if np.all(nc >= 0) and np.all(nc < len(map)):
      nc_t = tuple(nc)
      if  nc_t not in visited and map[nc_t] != "#" and (nc_t not in costs or len(visited) < costs[nc_t]):
        costs[nc_t] = len(visited) + 1
        visited.add(nc_t)
        if solve(map, nc, visited.copy()):
          return True
          # solved = True

  return solved

def main():
  # sys.setrecursionlimit(10000)

  with open("test-input.txt", "r") as file:
    map = []
    for line in file:
      map.append(list(line.strip()))
    map = np.array(map)

  start = np.argwhere(map == "S")[0]
  end = np.argwhere(map == "E")[0]

  solve(map, start, set())

  print(len(solutions), len(sorted(solutions)[0]) - 1)
  # print(len(solutions) - 1, solutions[0])


if __name__ == "__main__":
  main()