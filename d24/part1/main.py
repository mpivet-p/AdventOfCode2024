import re

value_pattern = re.compile(r"(.[^:]+): (\d+)")
instruction_pattern = re.compile(r"(\w+) (\w+) (\w+) -> (\w+)")

def exec(values, instruction):
  if instruction[1] == "XOR":
    op = values[instruction[0]] ^ values[instruction[2]]
  elif instruction[1] == "OR":
    op = values[instruction[0]] | values[instruction[2]]
  else:
    op = values[instruction[0]] & values[instruction[2]]
  values[instruction[3]] = op

def main():
  instructions = []
  values = {}

  with open("input.txt", "r") as file:
    for line in file:
      value_m = value_pattern.match(line)
      instruction_m = instruction_pattern.match(line)

      if value_m:
        key, value = value_m.groups()
        values[key] = int(value)
      elif instruction_m:
        instructions.append(instruction_m.groups())

  while True:
    todel = []
    for ins in instructions:
      if ins[0] in values and ins[2] in values:
        exec(values, ins)
        instructions.remove(ins)
        break
    #     todel.append(ins)
    # for e in todel:
    #   instructions.remove(e)
    if len(instructions) == 0:
      break

  result = ""
  for v in sorted(values):
    if v[0] == "z":
      result = str(values[v]) + result
  print(result, int(result, 2))
    # print(f"{v}: {values[v]}")
if __name__ == "__main__":
  main()