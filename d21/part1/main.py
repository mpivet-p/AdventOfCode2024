import numpy as np

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

def shortest_sequence(kbd, sequence):
  ptr =   np.argwhere(kbd == "A")[0]
  instructions = []

  empty = np.argwhere(kbd==None)[0]

  for c in sequence:
    tgt = np.argwhere(kbd == c)[0]
    diff = tgt - ptr
    y = "^" * abs(diff[0]) if diff[0] < 0 else "v" * diff[0]
    x = "<" * abs(diff[1]) if diff[1] < 0 else ">" * diff[1]

    if tgt[1] == empty[1] and empty[0] == ptr[0]:
      instructions.append(y + x)
    elif tgt[0] == empty[0] and empty[0] == ptr[0]:
      instructions.append(x + y)
    else:
      instructions.append((x, y) if x != "" and y != "" else x + y)

    instructions.append("A")
    ptr = tgt

  return instructions

def expand_seq(result, string, sequence):
  if len(sequence) == 0:
    result.append(string)
  elif type(sequence[0]) is not tuple:
    expand_seq(result, string + sequence[0], sequence[1:])
  else:
    expand_seq(result, string + sequence[0][0] + sequence[0][1], sequence[1:])
    expand_seq(result, string + sequence[0][1] + sequence[0][0], sequence[1:])

def main():
  with open("input.txt", "r") as file:
    codes = file.read().strip().split("\n")#[0:1]

  result = 0
  for co in codes:
    dir_keypad1 = []
    dir_keypad2 = []

    num_keypad = shortest_sequence(main_kbd, co)
    print(num_keypad)

    num = []
    expand_seq(num, "", num_keypad)

    for n1 in num:
      dir1 = shortest_sequence(sec_kbd, n1)
      expand_seq(dir_keypad1, "", dir1)

    for d1 in dir_keypad1:
      dir2 = shortest_sequence(sec_kbd, d1)
      expand_seq(dir_keypad2, "", dir2)

    result += len(sorted(dir_keypad2, key=len)[0]) * int(co[:3])

  print(result)

if __name__ == "__main__":
  main()