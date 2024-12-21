import numpy as np
import sys

solutions = []
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def solve(map, pos, visited):
  visited[tuple(pos)] = len(visited)
  solved = False

  if map[tuple(pos)] == "E":
    solutions.append(visited)
    return True
  
  next_pos = dirs + pos
  for nc in next_pos:
    if np.all(nc >= 1) and np.all(nc < len(map) - 1):
      nc_t = tuple(nc)
      if nc_t not in set(visited) and map[nc_t] != "#":
        if solve(map, nc, visited.copy()):
          solved = True

  return solved

def cheats(solution):
  possible_cheats = []

  for pos in solution:
    for pt in solution:
      if tuple(pos) != tuple(pt):
        manhattan_distance = abs(pos[0] - pt[0]) + abs(pos[1] - pt[1])
        if manhattan_distance < 20 and tuple(pt) in solution and solution[tuple(pt)] > solution[tuple(pos)]:
          dist = solution[tuple(pt)] - solution[tuple(pos)]
          if dist > manhattan_distance:
            possible_cheats.append((dist - manhattan_distance, tuple(pos), tuple(pt)))

  return possible_cheats
  
def main():
  sys.setrecursionlimit(10000)

  with open("test-input.txt", "r") as file:
    map_ = []
    for line in file:
      map_.append(list(line.strip()))
    map_ = np.array(map_)

  start = np.argwhere(map_ == "S")[0]

  solve(map_, start, {})
  ref = len(solutions[0]) - 1

  possible_cheats = cheats(solutions[0])

  print(f"Reference: {ref}")

  possible_cheats = sorted([n[0] for n in possible_cheats])
  # print(sum([1 if pc >= 100 else 0 for pc in possible_cheats]))


  cheats_ = {}
  for n in possible_cheats:
    if n not in cheats_ and n >= 50:
      cheats_[n] = possible_cheats.count(n)
      print(f"{n:3} -> {cheats_[n]}")

if __name__ == "__main__":
  main()