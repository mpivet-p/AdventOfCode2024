import numpy as np
import sys
from functools import lru_cache

main_kbd = np.array([
  ["7", "8", "9"],
  ["4", "5", "6"],
  ["1", "2", "3"],
  [None, "0", "A"]
])

sec_kbd = np.array([
  [None, "^", "A"],
  ["<", "v", ">"]
])

directions = {">": (0, 1), "^": (-1, 0), "v": (1, 0), "<": (0, -1), "A": (0, 0)}

def get_sequences(kbd, a, b):
  pos = np.argwhere(kbd == a)[0]
  tgt = np.argwhere(kbd == b)[0]

  diff = tgt - pos
  y = "^" * abs(diff[0]) if diff[0] < 0 else "v" * diff[0]
  x = "<" * abs(diff[1]) if diff[1] < 0 else ">" * diff[1]

  instructions = []
  moves = []
  permutations(moves, "", x, y)
  for t in moves:
    tmp_pos = pos.copy()
    possible = True

    for ins in t[:-1]:
      tmp_pos += directions[ins]
      if kbd[tuple(tmp_pos)] == None:
        possible = False
        break
    if possible:
      instructions.append(t)
  
  return instructions

def permutations(result, string, a, b):
  if len(a) == 0:
    result.append(string + b + "A")
  elif len(b) == 0:
    result.append(string + a + "A")
  else:
    permutations(result, string + a[0], a[1:], b)
    permutations(result, string + b[0], a, b[1:])

@lru_cache(None)
def get_instr_length(orig, dest, depth):
  if depth == 0:
    instr = get_sequences(sec_kbd, orig, dest)
    return min([len(e) for e in instr])
  
  sequences = get_sequences(sec_kbd if depth < 25 else main_kbd, orig, dest)
  min_length = 2 ** 63
  for seq in sequences:
    seq = "A" + seq
    length = 0
    for i in range(len(seq) - 1):
      length += get_instr_length(seq[i], seq[i + 1], depth - 1)

    min_length = min(min_length, length)
  return min_length

def main():
  with open("input.txt", "r") as file:
    codes = file.read().strip().split("\n")

  result = 0
  for co in codes:
    co = "A" + co
    length = 0

    for i in range(len(co) - 1):
      length += get_instr_length(co[i], co[i + 1], 25)
    result += length * int(co[1:4])
  print(result)

if __name__ == "__main__":
  main()