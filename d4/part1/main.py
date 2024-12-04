def main():

  map = []

  with open("test-input.txt", "r") as file:
    for line in file:
      map.append(list(line.strip()))

  limit_y = len(map)
  limit_x = len(map[0])

  count = 0

  for y in range(limit_y):
    for x in range(limit_x):
      if map[y][x] == "X":
        if y >= 3:
          if map[y - 1][x] == "M" and map[y - 2][x] == "A" and map[y - 3][x] == "S":
            count += 1
          if x >= 3:
            if map[y - 1][x - 1] == "M" and map[y - 2][x - 2] == "A" and map[y - 3][x - 3] == "S":
              count += 1
          if limit_x - x > 3:
            if map[y - 1][x + 1] == "M" and map[y - 2][x + 2] == "A" and map[y - 3][x + 3] == "S":
              count += 1  

        if limit_x - x > 3:
          if map[y][x + 1] == "M" and map[y][x + 2] == "A" and map[y][x + 3] == "S":
            count += 1
        if x >= 3:
          if map[y][x - 1] == "M" and map[y][x - 2] == "A" and map[y][x - 3] == "S":
            count += 1

        if limit_y - y > 3:
          if map[y + 1][x] == "M" and map[y + 2][x] == "A" and map[y + 3][x] == "S":
            count += 1
          if x >= 3:
            if map[y + 1][x - 1] == "M" and map[y + 2][x - 2] == "A" and map[y + 3][x - 3] == "S":
              count += 1
          if limit_x - x > 3:
            if map[y + 1][x + 1] == "M" and map[y + 2][x + 2] == "A" and map[y + 3][x + 3] == "S":
              count += 1

  print(count)

if __name__ == "__main__":
  main()