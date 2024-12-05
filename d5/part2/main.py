import re

def sort_updates(updates, rules):
  for i in range(len(updates) - 1, 0, -1):
    prev = set(updates[:i])
    if rules.get(updates[i]) and prev.intersection(rules[updates[i]]):
      to_pop = prev.intersection(rules[updates[i]])
      updates = [e for e in updates if e not in to_pop]
      updates += to_pop
      return sort_updates(updates, rules)

  return updates


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
        sorted_update = sort_updates(u, rules)
        result += sorted_update[len(sorted_update) // 2]
        break
  
  print(result)

if __name__ == "__main__":
  main()