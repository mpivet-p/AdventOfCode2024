directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def is_loop(map, x, y):
  visited = set()
  drn = 0

  while True:
    if (drn, y, x) not in visited:
      visited.add((drn, y, x))
    else:
      return True

    next_y = y + directions[drn][0]
    next_x = x + directions[drn][1]

    if next_y < 0 or next_x < 0 or next_y >= len(map) or next_x >= len(map[0]):
      break

    if map[next_y][next_x] == "#":
      drn = (drn + 1) % 4
    else:
      y = next_y
      x = next_x

  return False

def main():

  map = []

  with open("input.txt", "r") as file:
    for line in file:
      map.append(list(line.strip()))
      if "^" in line:
        x = line.index("^")
        y = len(map) - 1

  count = 0

  for i in range(len(map)):
    for j in range(len(map[0])):
      if map[i][j] == ".":
        map[i][j] = "#"
        count += is_loop(map, x, y)
        map[i][j] = "."

  print(f"{count=}")

if __name__ == "__main__":
  main()