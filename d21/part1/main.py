import numpy as np
from itertools import product

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

def shortest_sequence(kbd, sequence):
  ptr = np.argwhere(kbd == "A")[0]
  instructions = []

  for c in sequence:
    tgt = np.argwhere(kbd == c)[0]
    diff = tgt - ptr
    y = "^" * abs(diff[0]) if diff[0] < 0 else "v" * diff[0]
    x = "<" * abs(diff[1]) if diff[1] < 0 else ">" * diff[1]

    tmp = []
    moves = []
    permutations(moves, "", x, y)
    for t in moves:
      pos = ptr.copy()
      possible = True

      for ins in t[:-1]:
        pos += directions[ins]
        if kbd[tuple(pos)] == None:
          possible = False
          break
      if possible:
        tmp.append(t)
    
    instructions.append(tmp)
    ptr = tgt

  return ["".join(x) for x in product(*instructions)]

def permutations(result, string, a, b):
  if len(a) == 0:
    result.append(string + b + "A")
  elif len(b) == 0:
    result.append(string + a + "A")
  else:
    permutations(result, string + a[0], a[1:], b)
    permutations(result, string + b[0], a, b[1:])

def main():
  with open("input.txt", "r") as file:
    codes = file.read().strip().split("\n")

  result = 0
  for co in codes:
    numpad = shortest_sequence(main_kbd, co)

    keypad1 = []
    for num in numpad:
      keypad1 += shortest_sequence(sec_kbd, num)
    
    keypad2 = []
    for kp1 in keypad1:
      keypad2 += shortest_sequence(sec_kbd, kp1)

    result += len(sorted(keypad2, key=len)[0]) * int(co[:3])

  print(result)

if __name__ == "__main__":
  main()