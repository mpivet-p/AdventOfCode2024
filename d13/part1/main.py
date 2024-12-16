import re

def main():
  with open("input.txt", "r") as file:
    i = 0
    inputs = []
    for line in file:
      if i % 4 == 3:
        pass
      elif i % 4 == 2:
        inputs[i // 4]["Prize"] = [int(n) for n in re.findall(r"Prize: X=(\d+), Y=(\d+)", line)[0]]
      else:
        if i % 4 == 0:
          inputs.append({})
        inputs[i // 4][("ButtonA", "ButtonB")[i % 4]] = [int(n) for n in re.findall(r"Button .: X\+(\d+), Y\+(\d+)", line)[0]]
      i += 1

  solutions = []
  for machine in inputs:
    i = 0
    j = 0
    while machine["ButtonA"][0] * i + machine["ButtonB"][0] * j <= machine["Prize"][0]\
      and machine["ButtonA"][1] * i + machine["ButtonB"][1] * j <= machine["Prize"][1]:
      while machine["ButtonA"][0] * i + machine["ButtonB"][0] * j <= machine["Prize"][0]\
      and machine["ButtonA"][1] * i + machine["ButtonB"][1] * j <= machine["Prize"][1]:
        if machine["ButtonA"][0] * i + machine["ButtonB"][0] * j == machine["Prize"][0]\
      and machine["ButtonA"][1] * i + machine["ButtonB"][1] * j == machine["Prize"][1]:
          solutions.append((i, j))
          i += 10
          j += 10
          break
        j += 1
      j = 0
      i += 1

  print(sum([s[0] * 3 + s[1] for s in solutions]))

if __name__ == "__main__":
  main()