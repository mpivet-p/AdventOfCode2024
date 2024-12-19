import numpy as np
import sys

map_size = 71
solution = set()
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
costs = {}

def solve(bytes_, pos, visited):
  if tuple(pos) == (map_size -1, map_size - 1):
    global solution
    solution = visited
    return True
  
  visited.add(tuple(pos))

  next_pos = pos + directions
  for nc in next_pos:
    if np.all(nc < map_size) and np.all(nc >= 0) and tuple(nc) not in visited\
      and (tuple(nc) not in costs or costs[tuple(nc)] > len(visited) + 1)\
        and tuple(nc) not in bytes_:
      costs[tuple(nc)] = len(visited) + 1
      if solve(bytes_, nc, visited.copy()):
        return True

  return False

def main():
  bytes_ = []
  with open("input.txt", "r") as file:
    for line in file:
      bytes_.append(tuple([int(n) for n in line.split(",")]))

  for i in range(2000, len(bytes_)):
    if len(solution) > 0 and bytes_[i] not in solution:
      continue

    solution.clear()
    costs[(0, 0)] = 0

    if not solve(set(bytes_[:i + 1]), np.array((0, 0)), set()):
      print(f"{bytes_[i]} is not solvable (index {i})!")
      break
    else:
      print(f"Index {i}: successful.")
    costs.clear()

if __name__ == "__main__":
  main()