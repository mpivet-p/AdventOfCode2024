def main():

  map = []

  with open("input.txt", "r") as file:
    for line in file:
      map.append(list(line.strip()))
      if "^" in line:
        x = line.index("^")
        y = len(map) - 1

  visited = set()
  drn = 0
  directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

  while True:
    if (y, x) not in visited:
      visited.add((y, x))

    next_y = y + directions[drn][0]
    next_x = x + directions[drn][1]

    if next_y < 0 or next_x < 0 or next_y >= len(map) or next_x >= len(map[0]):
      break

    if map[next_y][next_x] == "#":
      drn = (drn + 1) % 4
    else:
      y = next_y
      x = next_x


  print(f"{len(visited)=}")

if __name__ == "__main__":
  main()