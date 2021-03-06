import json
import random

for file in ["data_scenarios_a_example", "data_scenarios_b_mumbai", "data_scenarios_c_metropolis", "data_scenarios_d_polynesia", "data_scenarios_e_sanfrancisco", "data_scenarios_f_tokyo"]:
#for file in ["data_scenarios_b_mumbai"]:
#for file in ["data_scenarios_a_example"]:
  with open('../parsed/'+file+'.json') as json_file:
    entities = json.load(json_file)
  no_buildings = len(entities["buildings"])
  used_fields = set()
  buildings_copy = list(entities["buildings"])
  for i in range(len(entities["antennas"])):
    if i < no_buildings:
      building = buildings_copy.pop(random.randint(0, len(buildings_copy)-1))
      entities["antennas"][i]["x"] = building["x"]
      entities["antennas"][i]["y"] = building["y"]
    else:
      while True:
        x = random.randint(0, entities["grid_width"]-1)
        y = random.randint(0, entities["grid_height"]-1)
        if not ((x,y) in used_fields):
          used_fields.add((x,y))
          entities["antennas"][i]["x"] = x
          entities["antennas"][i]["y"] = y
          break
  print("PLACED")
  with open("../placed/"+file + ".json", 'w') as fp:
    json.dump(entities, fp)