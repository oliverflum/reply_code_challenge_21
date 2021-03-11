import json
import random
from scipy.spatial import distance

def calcScore(buildings, antennas, all_connected_bonus):
    score = 0
    allConnected = True
    for b in buildings:
        tmp_max = 0
        connected = False
        for a in antennas:
            tmp_dist = calcDist(a,b)

            # no connection
            if tmp_dist > a["range"]:
                continue
                
            # OK
            tmp_score = b["speed"] * a["speed"] - b["latency"] * tmp_dist
            connected = True
            if tmp_score > tmp_max:
                tmp_max = tmp_score
        if connected == False:
            allConnected = False
        score += tmp_max
    
    if allConnected == True:
        score += all_connected_bonus  
    return score

# calculate distance
def calcDist(a,b):
    return distance.cityblock([a["x"], a["y"]], [b["x"], b["y"]])

for file in ["data_scenarios_a_example", "data_scenarios_b_mumbai", "data_scenarios_c_metropolis", "data_scenarios_d_polynesia", "data_scenarios_e_sanfrancisco", "data_scenarios_f_tokyo"]:
#for file in ["data_scenarios_b_mumbai"]:
#for file in ["data_scenarios_a_example"]:
  with open('parsed/'+file+'.json') as json_file:
    entities = json.load(json_file)
  no_buildings = len(entities["buildings"])
  used_fields = set()
  for i in range(len(entities["antennas"])):
    if i < no_buildings:
      entities["antennas"][i]["x"] = entities["buildings"][i]["x"]
      entities["antennas"][i]["y"] = entities["buildings"][i]["y"]
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
for file in ["data_scenarios_a_example", "data_scenarios_b_mumbai", "data_scenarios_c_metropolis", "data_scenarios_d_polynesia", "data_scenarios_e_sanfrancisco", "data_scenarios_f_tokyo"]:
  with open("placed/"+file + ".json", 'w') as fp:
    json.dump(entities, fp)
    with open('placed/'+file+'.json') as json_file:
    entities = json.load(json_file)
  new_score = calcScore(entities["buildings"], entities["antennas"], entities["reward"])
  if new_score > entities['score']:
      print("publish me")
      print(new_score)
        os.remove('placed/'+file+'.json')
    with open('placed/'+file+'.json') as json_file:
      entities = json.load(json_file)
    no_placed_antennas = len(entities["antennas"])
    antennas = entities["antennas"]
    print(type(antennas))
    file_object=open("outputs/"+file+".out", "a+")
    file_object.write(str(no_placed_antennas)+"\n")
    for a in antennas:
      line = " ".join([str(a["index"]), str(a["x"]), str(a["y"])])
      file_object.write(str(line+"\n"))
