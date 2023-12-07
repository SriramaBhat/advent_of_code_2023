import numpy as np
input_path = "F:\\advent_of_code\\inputs\\day_6.txt"
with open(input_path, "r") as file:
  time_list = file.readline().strip().split(":")
  time_list = time_list[1].split()
  distance_list = file.readline().strip().split(":")
  distance_list = distance_list[1].split()
  time = int("".join(time_list))
  distance = int("".join(distance_list))
  
  distance_list = []
  for i in range(2, time):
    distance_list.append(i * (time - i))
  distance_list = np.array(distance_list)
  print(len(distance_list[distance_list > distance]))
  