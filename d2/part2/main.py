def is_report_safe(report):
  # Test for non-sorted list
  if report != sorted(report) and report != sorted(report, reverse=True):
    return False

  # Test for duplicates -> meaning levels non-increasing or non-decreasing
  if len(report) != len(set(report)):
    return False

  # Test for levels jumping more than 3
  for i in range(len(report) - 1):
    if abs(report[i] - report[i + 1]) > 3:
      return False
  
  return True


if __name__ == "__main__":

  reports = []

  # Open file and prepare the reports in a int format
  with open("input.txt", "r") as file:
    for line in file:
      reports.append([int(element) for element in line.split()])

  safe = 0

  # Iterate through the reports
  for r in reports:
    if is_report_safe(r):
      safe += 1
    else:
      for i in range(len(r)):
        copy_r = r[:]
        del copy_r[i]
        if is_report_safe(copy_r):
          safe += 1
          break


  print(safe)