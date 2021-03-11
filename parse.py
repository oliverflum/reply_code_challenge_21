import json


def parse(file_name):
  in_file = open("inputs/"+file_name + ".in", 'r')
  lines = in_file.readlines()

  dimensions = [int(lines[0].split(' ')[0]),int(lines[0].split(' ')[1])]
  print(dimensions)

  split_stats = lines[1].strip().split(' ')

  no_buildings = int(split_stats[0])
  no_antennas = int(split_stats[1])
  reward = int(split_stats[2])

  print(no_buildings, no_antennas, reward)

  buildings_start_index = 2
  buildings_end_index = buildings_start_index + no_buildings
  print("BUILDINGS", buildings_start_index, buildings_end_index)
  antennas_start_index = buildings_end_index
  antennas_end_index = len(lines)

  entities = {
    "score": 0,
    "grid_width": dimensions[0],
    "grid_height": dimensions[1],
    "buildings": [],
    "antennas": [],
    "reward": reward
  }

  for i in range(buildings_start_index, buildings_end_index):
    building_props = lines[i].strip().split(" ")
    entities["buildings"].append({
      "index": i-buildings_start_index,
      "x": building_props[0],
      "y": building_props[1],
      "latency": building_props[2],
      "speed": building_props[3]
    })

  for i in range(antennas_start_index, antennas_end_index):
    antenna_props = lines[i].strip().split(" ")
    entities["antennas"].append({
      "x": None,
      "y": None,
      "index": i-antennas_start_index,
      "range": antenna_props[0],
      "speed": antenna_props[1]
    })

  if len(entities["buildings"]) != no_buildings or len(entities["antennas"]) != no_antennas:
    100/0

  with open("parsed/"+file_name + ".json", 'w') as fp:
    json.dump(entities, fp)

for file in ["data_scenarios_a_example", "data_scenarios_b_mumbai", "data_scenarios_c_metropolis", "data_scenarios_d_polynesia", "data_scenarios_e_sanfrancisco", "data_scenarios_f_tokyo"]:
  parse(file)