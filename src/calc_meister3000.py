import json
import numpy
import random

total = 0
for file in ["data_scenarios_a_example", "data_scenarios_b_mumbai", "data_scenarios_c_metropolis", "data_scenarios_d_polynesia", "data_scenarios_e_sanfrancisco", "data_scenarios_f_tokyo"]:
  with open('../placed/'+file+'.json') as json_file:
    entities = json.load(json_file)
  grid_width = entities["grid_width"]
  grid_height = entities["grid_height"]
  bmap = numpy.zeros([grid_width, grid_height])
  for i in range(len(entities["buildings"])):
    b = entities["buildings"][i]
    bmap[b["x"], b["y"]] = i
  for antenna in entities["antennas"]:
    min_x = max(0,antenna["x"]-antenna["range"])
    min_y = max(0,antenna["y"]-antenna["range"])
    max_x = min(grid_width,antenna["x"]+antenna["range"]+1)
    max_y = min(grid_height,antenna["y"]+antenna["range"]+1)
    if min_x == max_x:
      x_range = [min_x]
    else:
      x_range = range(min_x, max_x)
    if min_y == max_y:
      y_range = [min_y]
    else:
      y_range = range(min_y, max_y)
    for x in x_range:
      for y in y_range:
        index = int(bmap[x,y])
        if index != 0:
          building = entities["buildings"][int(bmap[x,y])]
          dist = abs(building["x"]-antenna["x"])+abs(building["y"]-antenna["y"])
          ba_score = building["speed"]*antenna["speed"]-building["latency"]*dist
          if not "scores" in building:
            building["scores"] = []
          building["scores"].append(ba_score)
  new_score = 0
  reward = True
  for building in entities["buildings"]:
    if "scores" in building:
      new_score += max(building["scores"])
    else:
      reward = False

  print("SCORE " + file + ": " + str(new_score))
  total += new_score

print("TOTAL: " + str(total))