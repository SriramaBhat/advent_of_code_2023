input_path = "F:\\advent_of_code\\inputs\\day1.txt"
with open(input_path, "r") as inp:
  ip = inp.readlines()
  for i in range(len(ip)):
    ip[i] = ip[i].strip()
  
  cali_sum = 0
  for cali in ip:
    num = 0    
    for c in cali:
      if c.isdigit():
        num += int(c)
        break
    
    num *= 10
    for i in range(len(cali) - 1, -1, -1):
      if cali[i].isdigit():
        num += int(cali[i])
        break
    
    cali_sum += num
  print(cali_sum)
