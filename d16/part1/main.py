import numpy as np
import sys

solutions = []
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
directions_names = [">", "v", "<", "^"]
costs = {}

def get_maze(filename):
  maze = []
  with open(filename, "r") as file:
    for line in file:
      maze.append(list(line.strip()))
  
  maze = np.array(maze)
  start = np.array(list(zip(*np.where(maze == "S")))[0])
  start = np.argwhere(maze == "S")[0]

  return maze, start

def solve(map, pos, visited, cost, dirn):
  if map[tuple(pos)] == "E":
    solutions.append(cost)
    return True

  visited.add(tuple(pos))
  next_pos = pos + directions
  solved = False
  for i, np in enumerate(next_pos):
    if tuple(np) not in visited and map[tuple(np)] != "#":
      tmp_cost = cost + 1 + [0, 1000, 2000, 1000][abs(dirn - i)]

      if not tuple(np) in costs or tmp_cost <= costs[tuple(np)]:
        costs[tuple(np)] = tmp_cost
        if solve(map, np, visited.copy(), tmp_cost, i):
          solved = True

  return solved

def main():
  maze, start = get_maze("test-input.txt")
  sys.setrecursionlimit(4000)

  solve(maze, start, set(), 0, 0)

  print(solutions)
  print(sorted(solutions)[0])

if __name__ == "__main__":
  main()