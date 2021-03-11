def calcScore(buildings, antennas, reward)
for file in ["data_scenarios_a_example", "data_scenarios_b_mumbai", "data_scenarios_c_metropolis", "data_scenarios_d_polynesia", "data_scenarios_e_sanfrancisco", "data_scenarios_f_tokyo"]:
  with open('placed/'+file+'.json') as json_file:
    entities = json.load(json_file)
  new_score = calcScore(entities["buildings"], entities["antennas"], entities["reward"])
  if new_score > entities['score']:
      print("publish me")
      print(new_score)