import numpy as np

explored = set()
deltas = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def explore(map, coords):
  new_coords = coords + deltas
  explored.add(tuple(coords))

  perimeter = 0
  area = 1

  for nc in new_coords:
    if np.all(nc >= 0) and np.all(nc < len(map)) and map[nc[0]][nc[1]] == map[coords[0]][coords[1]]:
      if (nc[0], nc[1]) not in explored:
        tmp = explore(map, nc)
        area += tmp[0]
        perimeter += tmp[1]
    else:
      perimeter += 1

  return (area, perimeter)


def main():
  with open("input.txt", "r") as file:
    map = []
    for line in file:
      map.append(list(line.strip()))
  
  zones = []

  for i, line in enumerate(map):
    for j in range(len(line)):
      if (i, j) not in explored:
        zones.append(explore(map, np.array([i, j])))

  # print(zones)
  print(sum([a * b for a, b in zones]))
  # print(map)

if __name__ == "__main__":
  main()