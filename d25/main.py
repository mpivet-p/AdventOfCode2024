import numpy as np

def main():
  with open("input.txt", "r") as file:
    locks = []
    keys = []
    for kl in file.read().split("\n\n"):
      shape = list(zip(*kl.split("\n")))
      if kl[0:5] == "#####":
        locks.append(np.array([e.count("#") - 1 for e in shape]))
      else:
        keys.append(np.array([e.count("#") - 1 for e in shape]))

  count = 0
  for lock in locks:
    for key in keys:
      tmp = lock + key
      if np.all(tmp <= 5):
        count += 1

  print(count)

if __name__ == "__main__":
  main()