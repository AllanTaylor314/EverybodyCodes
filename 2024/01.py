with open("everybody_codes_e2024_q1_p1.txt") as f:
    data = f.read().strip()
    print(data.count("B")+data.count("C")*3)

costs = {"A":0,"B":1,"C":3,"D":5,"x":-2}
with open("everybody_codes_e2024_q1_p2.txt") as f:
    data = f.read().strip()
    pairs = [data[i:i+2] for i in range(0,len(data),2)]
    print(sum(max(0,sum(map(costs.get,pair))+2) for pair in pairs))
costs = {"A":0,"B":1,"C":3,"D":5,"x":0}
x_cost = {0:3*2,1:2*1,2:0,3:0}
with open("everybody_codes_e2024_q1_p3.txt") as f:
    data = f.read().strip()
    trips = [data[i:i+3] for i in range(0,len(data),3)]
    print(sum(sum(map(costs.get,trip)) + x_cost[trip.count("x")] for trip in trips))
