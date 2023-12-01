input_path = "F:\\advent_of_code\\inputs\\day1.txt"
with open(input_path, "r") as inp:
  ip = inp.readlines()
  for i in range(len(ip)):
    ip[i] = ip[i].strip()
  
  res = 0
  digit_strings = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
  for cali in ip:
    nums = []
    for idx, c in enumerate(cali):
      if c.isdigit():
        nums.append(c)
      for i, digit in enumerate(digit_strings):
        if cali[idx:].startswith(digit):
          nums.append(str(i+1))
    res += int(nums[0] + nums[-1])
  print(res)
           