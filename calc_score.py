
from scipy.spatial import distance

# building:
# x,y,latency,speed

# antennas:
# x,y,range,speed
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


antennas = [
  {
      "x": 12,
      "y": 3,
      "range": 2,
      "speed": 100
  },
  {
      "x": 2,
      "y": 4,
      "range": 4,
      "speed": 10
  },
  {
      "x": 0,
      "y": 7,
      "range": 1,
      "speed": 50
  },
  {
      "x": 11,
      "y": 8,
      "range": 2,
      "speed": 40
  },
]

buildings = [
    {
        "x": 0,
        "y": 7,
        "latency": 3,
        "speed": 20
    },
    {
        "x": 12,
        "y": 2,
        "latency": 2,
        "speed": 14
    },
    {
        "x": 2,
        "y": 4,
        "latency": 1,
        "speed": 32
    },
    {
        "x": 10,
        "y": 7,
        "latency": 4,
        "speed": 44
    },
    {
        "x": 11,
        "y": 8,
        "latency": 3,
        "speed": 23
    }
]
# calculate distance
def calcDist(a,b):
    return distance.cityblock([a["x"], a["y"]], [b["x"], b["y"]])
