import numpy as np

explored = set()
deltas = [(0, 1), (1, 0), (0, -1), (-1, 0)]
memory = {}

def is_valid(coords, map, zone):
  return np.all(coords >= 0) and np.all(coords < len(map)) and map[coords[0]][coords[1]] == zone

def explore_edges(coords, map, i, j, zone):
  tmp_coords = coords
  while True:
    tmp_coords = tmp_coords + deltas[(i + j) % 4]
    tmp_dt = tmp_coords + deltas[i]
    if (tmp_coords[0], tmp_coords[1]) not in explored\
      and is_valid(tmp_coords, map, zone)\
        and not is_valid(tmp_dt, map, zone):
      memory.setdefault((tmp_coords[0], tmp_coords[1]), []).append(deltas[i])
    else:
      return

def explore(map, coords):
  zone = map[coords[0]][coords[1]]
  explored.add(tuple(coords))

  new_coords = list(coords + deltas)
  perimeter = 0
  area = 1

  visited = [item for nc in new_coords for item in memory.get((nc[0], nc[1]), [])]
  for i, nc in enumerate(new_coords):
    if not is_valid(nc, map, zone):
      memory.setdefault((coords[0], coords[1]), []).append(deltas[i])
      if deltas[i] not in visited:
        perimeter += 1
        explore_edges(coords, map, i, 1, zone)
        explore_edges(coords, map, i, 3, zone)

  for nc in new_coords:
    if (nc[0], nc[1]) not in explored and is_valid(nc, map, zone):
      tmp = explore(map, nc)
      area += tmp[0]
      perimeter += tmp[1]

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
        memory.clear()
        zones.append(explore(map, np.array([i, j])))

  print(sum([a * b for a, b in zones]))

if __name__ == "__main__":
  main()