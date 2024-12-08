def load_equations(filename):
  equations = []
  with open(filename, "r") as file:
    for line in file:
      a, b = line.split(": ")
      equations.append([int(a), [int(e) for e in b.split(" ")]])
  
  return equations

def get_all_comb(length, op_str):
  if len(op_str) == length:
    return [op_str]
  
  res = []
  res += get_all_comb(length, op_str + "*")
  res += get_all_comb(length, op_str + "+")
  res += get_all_comb(length, op_str + "|")

  return res

def solve(target, equation, operators):
  for op in operators:
    result = equation[0]

    for i in range(1, len(equation)):
        if op[i - 1] == "*":
          result *= equation[i]
        elif op[i - 1] == "|":
          result = int(str(result) + str(equation[i]))
        else:
          result += equation[i]

    if result == target:
      return True

  return False

def main():
  equations = load_equations("input.txt")
  result = 0

  for e in equations:
    operators = get_all_comb(len(e[1]) - 1, "")
    if solve(e[0], e[1], operators):
      result += e[0]

  print(result)

if __name__ == "__main__":
  main()