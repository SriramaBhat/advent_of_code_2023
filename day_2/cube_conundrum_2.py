input_path = "F:\\advent_of_code\\inputs\\day_2.txt"
with open(input_path, "r") as inp:
  ip = inp.readlines()
  for i in range(len(ip)):
    ip[i] = ip[i].strip()
  
  games = {}  
  for i in ip:
    temp = i.split(":")
    game_and_id = temp[0]
    game_and_id = game_and_id.split()
    sets = temp[1].split(";")
    for j in range(len(sets)):
      sets[j] = sets[j].split(",")
      for k in range(len(sets[j])):
        sets[j][k] = sets[j][k].strip()
    games[int(game_and_id[1])] = sets
  
power_sum = 0
for key, val in games.items():  
  power, max_red, max_green, max_blue = 0, 0, 0, 0
  for v in val:
    for b in v:
      temp = b.split()
      if temp[1] == "red":
        max_red = int(temp[0]) if int(temp[0]) > max_red else max_red
      if temp[1] == "green":
        max_green = int(temp[0]) if int(temp[0]) > max_green else max_green
      if temp[1] == "blue":
        max_blue = int(temp[0]) if int(temp[0]) > max_blue else max_blue
  power = max_red * max_green * max_blue
  power_sum += power
print(power_sum)
  