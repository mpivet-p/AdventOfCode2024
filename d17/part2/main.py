import re

solutions = []

def combo(operand, registers):
  if operand <= 3:
    return operand
  return registers[chr(ord("A") + operand - 4)]

def adv(operand, registers, instruction_pointer, output): # 0
  registers["A"] = registers["A"] >> combo(operand, registers)

def bxl(operand, registers, instruction_pointer, output): # 1
  registers["B"] = registers["B"] ^ operand

def bst(operand, registers, instruction_pointer, output): # 2
  registers["B"] = combo(operand, registers) % 8

def jnz(operand, registers, instruction_pointer, output): # 3
  if registers["A"] != 0:
    instruction_pointer[0] = operand - 2

def bxc(operand, registers, instruction_pointer, output): # 4
  registers["B"] = registers["B"] ^ registers["C"]

def out(operand, registers, instruction_pointer, output): # 5
  output.append(combo(operand, registers) % 8)

def bdv(operand, registers, instruction_pointer, output): # 6
  registers["B"] = registers["A"] // (2 ** combo(operand, registers))

def cdv(operand, registers, instruction_pointer, output): # 7
  registers["C"] = registers["A"] // (2 ** combo(operand, registers))

instr_set = [adv, bxl, bst, jnz, bxc, out, bdv, cdv]

def program_(program, registers, output):
  instruction_pointer = [0]

  while instruction_pointer[0] < len(program) - 1:
    instr_set[program[instruction_pointer[0]]](program[instruction_pointer[0] + 1], registers, instruction_pointer, output)
    instruction_pointer[0] += 2

  return output

def solve(program, registers):
  for j in range(8):
    registers["A"] += 1

    out = program_(program, registers.copy(), [])

    if out == program[len(program) - len(out):]:
      if len(out) == len(program):
        solutions.append(registers["A"])
        return

      solve(program, {**registers, "A": registers["A"] << 3})


def main():
  registers = {}

  with open("input.txt", "r") as file:
    content = file.read()
    for r in re.findall(r"Register (A|B|C): (\d+)", content):
      registers[r[0]] = int(r[1])
    program = [int(i) for i in re.findall(r"Program: (.*)$", content)[0].split(",")]
  
  solve(program, registers)
  print(sorted(solutions)[0])


if __name__ == "__main__":
  main()