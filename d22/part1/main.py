def mix_and_prune(n, secret):
  return (n ^ secret) % 16777216

def mult(n):
  result = n * 64
  return mix_and_prune(result, n)

def div(n):
  result = int(n / 32)
  return mix_and_prune(result, n)


def mult2(n):
  result = n * 2048
  return mix_and_prune(result, n)

def generate_secret(n):
  for _ in range(2000):
    n = mult2(div(mult(n)))
  return n


def main():
  with open("input.txt", "r") as file:
    numbers = [int(n) for n in file]

  result = 0
  for n in numbers:
    result += generate_secret(n)
  print(f"Result: {result}")

if __name__ == "__main__":
  main()