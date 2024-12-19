import numpy as np
import sys

sys.setrecursionlimit(3000)

map_size = 71
limit = map_size - 1
solutions = []
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
costs = {}

def solve(maze, pos, visited):
  if tuple(pos) == (limit, limit):
    solutions.append((len(visited), visited))
    return True
  
  visited.add(tuple(pos))

  next_pos = pos + directions
  for nc in next_pos:
    if np.all(nc < map_size) and np.all(nc >= 0) and tuple(nc) not in visited and (tuple(nc) not in costs or costs[tuple(nc)] > len(visited) + 1) and maze[tuple(nc)] != 1:
      costs[tuple(nc)] = len(visited) + 1
      solve(maze, nc, visited.copy())

  return False

def main():
  memory = np.zeros((map_size, map_size))
  with open("input.txt", "r") as file:
    size = 1051
    for line in file:
      if size == 0:
        break
      x, y = [int(n) for n in line.split(",")]
      memory[y, x] += 1
      size -= 1

  costs[(0, 0)] = 0
  solve(memory, np.array((0, 0)), set())
  print(sorted([sol[0] for sol in solutions]))


if __name__ == "__main__":
  main()