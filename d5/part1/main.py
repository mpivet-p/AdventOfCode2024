import re

def main():
  rules = {}
  updates = []

  with open("input.txt", "r") as file:
    for line in file:
      if re.match(r'\d+\|\d+', line):
        before, after = line.split("|")
        rules.setdefault(int(before), set()).add(int(after))
      elif re.match(r'(\d+,)+\d', line):
        updates.append([int(n) for n in line.strip().split(",")])

  result = 0
  for u in updates:
    prev = set()
    for i in range(1, len(u)):
      prev.add(u[i - 1])
      if rules.get(u[i]) and prev.intersection(rules[u[i]]):
        break
    else:
      result += u[len(u) // 2]
  
  print(result)

if __name__ == "__main__":
  main()