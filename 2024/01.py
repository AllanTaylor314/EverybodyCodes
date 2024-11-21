costs = {"A":0,"B":1,"C":3,"D":5,"x":0}
x_cost = {3:3*2,2:2*1,1:0,0:0}
for part in (1,2,3):
    with open(f"everybody_codes_e2024_q1_p{part}.txt") as f:
        data = f.read().strip()
    trips = [data[i:i+part] for i in range(0,len(data),part)]
    print(sum(sum(map(costs.get,trip)) + x_cost[part-trip.count("x")] for trip in trips))
