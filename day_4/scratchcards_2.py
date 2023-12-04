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
    v[0] = set(v[0])
    v[1] = set(v[1])
  
  card_count = len(cards) 
  temp1 = []
  temp2 = [1] * len(cards)
  for key, val in cards.items():
    power = len(val[0].intersection(val[1]))
    temp1.append(power)
      
  for i in range(card_count):
    duplicates = temp1[i]
    current = i + 1
    while duplicates > 0 and current < card_count:
      temp2[current] += temp2[i]
      duplicates -= 1
      current += 1
  print(sum(temp2))
