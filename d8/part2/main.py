import numpy as np

def get_map(filename):
  a_map = []
  antennas = {}
  with open(filename, "r") as file:
    for i, line in enumerate(file):
      a_map.append(list(line.strip()))
      for j, point in enumerate(a_map[i]):
        if point != ".":
          antennas.setdefault(point, []).append(np.array((i, j)))
  
  return np.array((len(a_map), len(a_map[0]))), antennas

def main():
  map, antennas = get_map("input.txt")

  antinodes = set()
  for freq in antennas:
    for antenna in antennas[freq]:
      antinodes.add(tuple(antenna))
      for pt in antennas[freq]:
        if not np.array_equal(antenna, pt):
          diff = antenna - pt
          i = 1
          while True:
            coords = antenna + diff * i
            if (coords < map).all() and np.all(coords >= 0):
              antinodes.add(tuple(coords))
            else:
              break
            i += 1

  print(len(antinodes))

if __name__ == "__main__":
  main()