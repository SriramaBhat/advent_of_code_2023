input_path = "F:\\advent_of_code\\inputs\\day_4.txt"
with open(input_path, "r") as file:
  inp = file.readlines()
  ip = [i.strip() for i in inp] 
  cards = {}
  for i in ip:
    temp = i.split(":")
    cards[int(temp[0].split()[1])] = temp[1].strip().split("|")
  for v in cards.values():
    v[0] = v[0].strip()
    v[1] = v[1].strip()
    v[0] = [int(i) for i in v[0].split()]
    v[1] = [int(i) for i in v[1].split()]
  value = 0
  for key, val in cards.items():
    winning = set(val[0])
    present = set(val[1])
    power = len(winning.intersection(present))
    if power == 0:
      continue
    else:
      value += 2**(power-1)
  print(value)
