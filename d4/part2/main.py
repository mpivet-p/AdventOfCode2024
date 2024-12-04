possibilities = ("MSMS", "MMSS", "SSMM", "SMSM")

def main():
  map = []

  with open("input.txt", "r") as file:
    for line in file:
      map.append(list(line.strip()))

  limit_y = len(map)
  limit_x = len(map[0])
  count = 0

  for y in range(limit_y):
    for x in range(limit_x):

      if map[y][x] == "A":
        cross = ""
        if y >= 1:
          if x >= 1:
            cross += map[y - 1][x - 1]
          if limit_x - x > 1:
            cross += map[y - 1][x + 1]

        if limit_y - y > 1:
          if x >= 1:
            cross += map[y + 1][x - 1]
          if limit_x - x > 1:
            cross += map[y + 1][x + 1]

        if cross in possibilities:
          count += 1

  print(count)

if __name__ == "__main__":
  main()