import numpy as np

def get_map(filename):
  mapedit = {"#": "##", "O": "[]", ".": "..", "@": "@."}
  map = []
  instructions = []

  with open(filename, "r") as file:
    for line in file:
      if "#" in line:
        s = "".join([mapedit[c] for c in line.strip()])
        map.append(list(s))
      elif line != "\n":
        instructions.extend([c for c in line.strip()])

  return np.array(map), instructions

def print_map(map):
  print("\n".join(["".join(row) for row in map]))

def move_horizontally(map, pos, dir):
  tmp = pos.copy()
  while map[tuple(tmp)] == "[" or map[tuple(tmp)] == "]":
    tmp += dir

  if map[tuple(tmp)] == "#":
    return False

  i = 0
  while not np.array_equal(tmp, pos):
    map[tuple(tmp)] = "[]"[(i + (dir[1] == 1))% 2]
    tmp -= dir
    i += 1

  return True

def check_vertically(map, pos, dir, caller):
  if map[tuple(pos)] == ".":
    return True
  elif map[tuple(pos)] == "#":
    return False
  elif pos[0] != caller[0]:
    if map[tuple(pos)] == "[":
      if check_vertically(map, pos + (0, 1), dir, pos) == False:
        return False
    else:
      if check_vertically(map, pos + (0, -1), dir, pos) == False:
        return False
  return check_vertically(map, pos + dir, dir, pos)

def move_vertically(map, pos, dir, caller, first):
  if map[tuple(pos)] == ".":
    map[tuple(pos)] = map[tuple(caller)]
    return

  move_vertically(map, pos + dir, dir, pos, False)

  if pos[0] != caller[0]:
    if map[tuple(pos)] == "[":
      move_vertically(map, pos + (0, 1), dir, pos, first)
    else:
      move_vertically(map, pos + (0, -1), dir, pos, first)

  if not first and pos[0] != caller[0]:
    map[tuple(pos)] = map[tuple(caller)]
  else:
    map[tuple(pos)] = "."


def move_or_push(map, pos, dir, old_pos):
  if dir[0] == 0:
    return move_horizontally(map, pos, dir)
  if check_vertically(map, pos, dir, old_pos):
    move_vertically(map, pos, dir, old_pos, True)
    return True
  return False

def main():
  map, instructions = get_map("input.txt")
  pos = np.argwhere(map=="@")[0]

  instr_set = {"<": (0, -1), "^": (-1, 0), ">": (0, 1), "v": (1, 0)}

  print_map(map)
  for ins in instructions:
    next_pos = pos + instr_set[ins]
    if map[tuple(next_pos)] == "." or move_or_push(map, np.copy(next_pos), instr_set[ins], pos):
      map[tuple(pos)] = "."
      map[tuple(next_pos)] = "@"
      pos = next_pos

  print(sum([y * 100 + x for y, x in zip(*np.where(map=="["))]))


if __name__ == "__main__":
  main()