from enum import Enum

class Dir(Enum):
  DOWN = 1
  UP = -1
  NONE = 0
  RIGHT = 1
  LEFT = -1

def check_direction(map, x, y, dy, dx):
  if map[y + 1 * dy.value][x + 1 * dx.value] == "M"\
    and map[y + 2 * dy.value][x + 2 * dx.value] == "A"\
      and map[y + 3 * dy.value][x + 3 * dx.value] == "S":
    return True

  return False


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

      if map[y][x] == "X":
        if y >= 3:
          count += check_direction(map, x, y, Dir.UP, Dir.NONE)
          if x >= 3:
            count += check_direction(map, x, y, Dir.UP, Dir.LEFT)
          if limit_x - x > 3:
            count += check_direction(map, x, y, Dir.UP, Dir.RIGHT)


        if limit_x - x > 3:
          count += check_direction(map, x, y, Dir.NONE, Dir.RIGHT)
        if x >= 3:
          count += check_direction(map, x, y, Dir.NONE, Dir.LEFT)

        if limit_y - y > 3:
          count += check_direction(map, x, y, Dir.DOWN, Dir.NONE)
          if x >= 3:
            count += check_direction(map, x, y, Dir.DOWN, Dir.LEFT)
          if limit_x - x > 3:
            count += check_direction(map, x, y, Dir.DOWN, Dir.RIGHT)

  print(count)

if __name__ == "__main__":
  main()