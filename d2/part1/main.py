if __name__ == "__main__":

  reports = []

  # Open file and prepare the reports in a int format
  with open("input.txt", "r") as file:
    for line in file:
      reports.append([int(element) for element in line.split()])

  safe = 0

  # Iterate through the reports
  for r in reports:
    # Test for non-sorted list
    if r != sorted(r) and r != sorted(r, reverse=True):
      continue

    # Test for duplicates -> meaning levels non-increasing or non-decreasing
    if len(r) != len(set(r)):
      continue

    # Test for levels jumping more than 3
    for i in range(len(r) - 1):
      if abs(r[i] - r[i + 1]) > 3:
        break
    else:
      safe += 1

  print(safe)