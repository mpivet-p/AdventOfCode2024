def checksum(disk):
  result = 0
  count = 0
  end = len(disk) - 1
  for i in range(len(disk)):
    # print(disk)
    if i % 2 == 1:
      while disk[i] > 0 and end > i:
        if disk[end] == 0:
          end -= 2
        else:
          result += count * int(end / 2)
          # print(f"end {count} * {int(end / 2)} = {count * int(end / 2)}")
          count += 1
          disk[end] -= 1
          disk[i] -= 1
    else:
      while disk[i] > 0:
        result += count * int(i / 2)
        # print(f"i {count} * {int(i / 2)} = {count * int(i / 2)}")
        count += 1
        disk[i] -= 1


  return result

def main():
  with open("input.txt", "r") as file:
    disk = [int(c) for c in file.read()]

  print(checksum(disk))

if __name__ == "__main__":
  main()