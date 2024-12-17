import numpy as np

def get_map(filename):
  with open(filename, "r") as file:
    map = []
    instructions = []
    for line in file:
      if "#" in line:
        map.append([c for c in line.strip()])
      elif line != "\n":
        instructions.extend([c for c in line.strip()])

  return np.array(map), instructions

def print_map(map):
  print("\n".join(["".join(row) for row in map]))

def move_or_push(map, pos, dir):
  while map[tuple(pos)] == "O":
    pos += dir

  if map[tuple(pos)] == "#":
    return False
  map[tuple(pos)] = "O"
  return True

def main():
  map, instructions = get_map("input.txt")
  pos = np.argwhere(map=="@")[0]

  instr_set = {"<": (0, -1), "^": (-1, 0), ">": (0, 1), "v": (1, 0)}

  for ins in instructions:
    # print(f"===[ {ins} ]===")
    next_pos = pos + instr_set[ins]
    if map[tuple(next_pos)] == "." or move_or_push(map, np.copy(next_pos), instr_set[ins]):
      map[tuple(pos)] = "."
      map[tuple(next_pos)] = "@"
      pos = next_pos

    # print_map(map)
  print(sum([y * 100 + x for y, x in zip(*np.where(map=="O"))]))


if __name__ == "__main__":
  main()