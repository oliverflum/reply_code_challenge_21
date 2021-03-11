import json

for file in ["data_scenarios_a_example", "data_scenarios_b_mumbai", "data_scenarios_c_metropolis", "data_scenarios_d_polynesia", "data_scenarios_e_sanfrancisco", "data_scenarios_f_tokyo"]:
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