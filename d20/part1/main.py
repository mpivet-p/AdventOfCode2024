import numpy as np
import sys

costs = {}
solutions = []
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def solve(map, pos, visited):
  visited[tuple(pos)] = len(visited)

  if map[tuple(pos)] == "E":
    solutions.append(visited)
    return True
  
  solved = False

  next_pos = dirs + pos
  for nc in next_pos:
    if np.all(nc >= 1) and np.all(nc < len(map) - 1):
      nc_t = tuple(nc)
      if nc_t not in set(visited) and map[nc_t] != "#":
        if solve(map, nc, visited.copy()):
          solved = True
  return solved

def cheats(map, solution):
  possible_cheats = []
  for i in range(1, len(map)- 1):
    for j in range(1, len(map) -1):
      if map[i, j] == "#":
        pp = dirs + np.array((i, j))
        pp = [tuple(pp[0]), tuple(pp[1]), tuple(pp[2]), tuple(pp[3])]
        if pp[0] in solution and pp[2] in solution:
          possible_cheats.append(((max(solution[pp[0]], solution[pp[2]]) - min(solution[pp[0]], solution[pp[2]])) - 2, (i, j)))
        if pp[1] in solution and pp[3] in solution:
          possible_cheats.append(((max(solution[pp[1]], solution[pp[3]]) - min(solution[pp[1]], solution[pp[3]])) - 2, (i, j)))

  return possible_cheats


def main():
  sys.setrecursionlimit(10000)

  with open("input.txt", "r") as file:
    map_ = []
    for line in file:
      map_.append(list(line.strip()))
    map_ = np.array(map_)

  start = np.argwhere(map_ == "S")[0]

  solve(map_, start, {})
  possible_cheats = cheats(map_, solutions[0])

  possible_cheats = [n[0] for n in possible_cheats]
  print(sum([1 if pc >= 100 else 0 for pc in possible_cheats]))

if __name__ == "__main__":
  main()