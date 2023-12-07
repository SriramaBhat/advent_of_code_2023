import numpy as np
input_path = "F:\\advent_of_code\\inputs\\day_6.txt"
with open(input_path, "r") as file:
  time_list = file.readline().strip().split(":")
  time_list = time_list[1].split()
  time_list = [int(i) for i in time_list]
  distance_list = file.readline().strip().split(":")
  distance_list = distance_list[1].split()
  distance_list = [int(i) for i in distance_list]
  
  counts = []
  for race in range(len(time_list)):
    distances = []
    for i in range(1, time_list[race]):
      distances.append(i * (time_list[race] - i))
    distances = np.array(distances)
    counts.append(len(distances[distances > distance_list[race]]))
  counts = np.array(counts)
  print(counts.prod())
  