input_path = "F:\\advent_of_code\\inputs\\day_2.txt"
with open(input_path, "r") as inp:
  ip = inp.readlines()
  for i in range(len(ip)):
    ip[i] = ip[i].strip()
  
  red_max, green_max, blue_max = 12, 13, 14
  possible_games = 0
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
    
  for key, val in games.items():
    flag = 0
    for v in val:
      for b in v:
        temp = b.split()
        if temp[1] == "red" and int(temp[0]) > red_max:
          flag = 1
          break
        if temp[1] == "green" and int(temp[0]) > green_max:
          flag = 1
          break
        if temp[1] == "blue" and int(temp[0]) > blue_max:
          flag = 1
          break
      if flag == 1:
        break
    if flag == 1:
      continue
    possible_games += key
  print(possible_games)
