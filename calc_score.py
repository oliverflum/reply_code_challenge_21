
from scipy.spatial import distance
import json

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

#for file in ["data_scenarios_a_example", "data_scenarios_b_mumbai", "data_scenarios_c_metropolis", "data_scenarios_d_polynesia", "data_scenarios_e_sanfrancisco", "data_scenarios_f_tokyo"]:
for file in ["data_scenarios_b_mumbai"]:
#for file in ["data_scenarios_a_example"]:
  with open('placed/'+file+'.json') as json_file:
    entities = json.load(json_file)
  new_score = calcScore(entities["buildings"], entities["antennas"], entities["reward"])
  if new_score > entities['score']:
      print("publish me")
      print(new_score)