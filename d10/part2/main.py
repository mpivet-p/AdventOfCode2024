import numpy as np

deltas = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def find_trailheads(coords, map):
  if map[coords[0], coords[1]] == 9:
    return 1

  new_coords = deltas + coords
  results = 0
  for nc in new_coords:
    if np.all((nc >= 0)&(nc < map.shape[0])) and map[nc[0], nc[1]] == (map[coords[0], coords[1]] + 1):# and tuple(nc) not in already_visited:
        results += find_trailheads(nc, map)

  return results

def main():
  with open("input.txt", "r") as file:
    tmp = []
    for line in file:
      tmp.append([int(c) if c != "." else -1 for c in line.strip()])
    map = np.array(tmp)

  zeros = np.where(map == 0)
  trailstarts = np.array(list(zip(zeros[0], zeros[1])))
  result = 0

  for t in trailstarts:
    result += find_trailheads(t, map)

  print(result)

if __name__ == "__main__":
  main()