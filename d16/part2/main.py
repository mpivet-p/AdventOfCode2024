import numpy as np
import sys
import matplotlib.pyplot as plt

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
    solutions.append((cost, visited))
    return True

  visited.add(tuple(pos))
  next_pos = pos + directions
  solved = False
  to_add = []
  for i, np in enumerate(next_pos):
    if tuple(np) not in visited and map[tuple(np)] != "#":
      tmp_cost = cost + 1 + [0, 1000, 2000, 1000][abs(dirn - i)]

      if not tuple(np) in costs or tmp_cost - 1001 <= costs[tuple(np)]:
        to_add.append((tuple(np), tmp_cost))
        if solve(map, np, visited.copy(), tmp_cost, i):
          solved = True

  for t in to_add:
    costs[tuple(t[0])] = t[1]

  return solved

def display_maze(maze_char, visited):
  maze_numeric = np.zeros_like(maze_char, dtype=int)
  maze_numeric[maze_char != '#'] = 1

  for v in visited:
    maze_numeric[v] = 10

  plt.figure(figsize=(6, 6))
  plt.imshow(maze_numeric, cmap="gray_r")
  start = np.argwhere(maze_char == 'S')[0]
  end = np.argwhere(maze_char == 'E')[0]
  plt.text(start[1], start[0], 'S', color='green', ha='center', va='center', fontsize=12, fontweight='bold')
  plt.text(end[1], end[0], 'E', color='red', ha='center', va='center', fontsize=12, fontweight='bold')

  plt.axis('off')
  plt.show()


def main():
  maze, start = get_maze("test-input.txt")
  sys.setrecursionlimit(4000)

  solve(maze, start, set(), 0, 0)
  result = set()
  lowest_cost = sorted([sol[0] for sol in solutions])[0]

  for sol in solutions:
    if lowest_cost == sol[0]:
      result = result.union(sol[1])
  print(len(result) + 1)

  display_maze(maze, result)

if __name__ == "__main__":
  main()