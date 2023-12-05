def find_initial_map(initials, k):
  for i in range(k):
    temp = file.readline()
    temp = file.readline()
    interval1 = []
    interval2 = []
    while temp.strip() != "":
      temp = temp.split()
      interval1.append([int(temp[1]), int(temp[1]) + int(temp[2]) - 1])
      interval2.append([int(temp[0]), int(temp[0]) + int(temp[2]) - 1])  
      temp = file.readline()
    
    initial_map = []
    for s in initials:
      flag = 0
      for i in range(len(interval1)):
        if s >= interval1[i][0] and s <= interval1[i][1]:
          flag = 1
          initial_map.append(interval2[i][0] + (s - interval1[i][0]))
      if flag == 0:
        initial_map.append(s)
    initials = initial_map
    initial_map = []
  return initials

input_path = "F:\\advent_of_code\\inputs\\day_5.txt"
with open(input_path, "r") as file:
  initials = file.readline().strip()
  initials = initials.split(":")[1].strip()
  initials = [int(i) for i in initials.split()]
  temp = file.readline().strip()
  location_mapping = find_initial_map(initials, 7)
  print(min(location_mapping))
