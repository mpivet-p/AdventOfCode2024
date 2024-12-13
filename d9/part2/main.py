def main():
  with open("input.txt", "r") as file:
    disk = [(int(i / 2) if i % 2 == 0 else None, int(c)) for i, c in enumerate(file.read())]

  end = len(disk) - 1
  while end > 0:
    if disk[end][0] is not None:
      free_blocks = list(filter(lambda x: x[0] < end and x[1][0] == None, enumerate(disk)))
      for b in free_blocks:
        if b[1][1] > disk[end][1]:
          disk[b[0]] = (None, b[1][1] - disk[end][1])
          disk.insert(b[0], disk[end])
          disk[end + 1] = (None, disk[end + 1][1])
          break
        elif b[1][1] == disk[end][1]:
          disk[b[0]] = disk[end]
          disk[end] = (None, disk[end][1])
          break
    end -= 1

  result = 0
  count = 0
  for e in disk:
    if e[0] is not None:
      for i in range(e[1]):
        result += count * e[0]
        # print(f"{count} * {e[0]} = {count * e[0]}")
        count += 1
    else:
      count += e[1]
  print(result)

if __name__ == "__main__":
  main()