import numpy as np

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
  nbrs = [n]
  for i in range(2000):
    n = mult2(div(mult(n)))
    nbrs.append(n)

  return np.array(nbrs)

def get_price_evolutions(price_evo, base):
    already_seen = set()
    price = base % 10
    diffs = price[1:] - price[:-1]
    price = np.delete(price, 0)
    for i in range(3, 2000):
      var = tuple(diffs[i - 3:i + 1])
      if var not in already_seen:
        already_seen.add(var)
        price_evo[var] = price_evo.get(var, 0) + price[i]

def main():
  with open("input.txt", "r") as file:
    numbers = [int(n) for n in file]

  price_evolutions = {}

  for n in numbers:
    base = generate_secret(n)
    get_price_evolutions(price_evolutions, base)

  print(f"Result: {max([price_evolutions[p] for p in price_evolutions])}")

if __name__ == "__main__":
  main()