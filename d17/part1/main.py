import re

instruction_pointer = 0
output = []

def combo(operand, registers):
  if operand <= 3:
    return operand
  return registers[chr(ord("A") + operand - 4)]

def adv(operand, registers):
  registers["A"] = registers["A"] // (2 ** combo(operand, registers))

def bxl(operand, registers):
  registers["B"] = registers["B"] ^ operand

def bst(operand, registers):
  registers["B"] = combo(operand, registers) % 8

def jnz(operand, registers):
  if registers["A"] != 0:
    global instruction_pointer
    instruction_pointer = operand - 2

def bxc(operand, registers):
  registers["B"] = registers["B"] ^ registers["C"]

def out(operand, registers):
  global output
  output.append(str(combo(operand, registers) % 8))

def bdv(operand, registers):
  registers["B"] = registers["A"] // (2 ** combo(operand, registers))

def cdv(operand, registers):
  registers["C"] = registers["A"] // (2 ** combo(operand, registers))

def main():
  registers = {}
  global instruction_pointer

  with open("input.txt", "r") as file:
    content = file.read()
    for r in re.findall(r"Register (A|B|C): (\d+)", content):
      registers[r[0]] = int(r[1])
    program = [int(i) for i in re.findall(r"Program: (.*)$", content)[0].split(",")]

  print(registers, program)
  instr_set = [adv, bxl, bst, jnz, bxc, out, bdv, cdv]

  while instruction_pointer < len(program) - 1:
    instr_set[program[instruction_pointer]](program[instruction_pointer + 1], registers)
    instruction_pointer += 2

  print(",".join(output))

if __name__ == "__main__":
  main()