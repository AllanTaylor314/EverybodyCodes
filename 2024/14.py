def load_file(part):
    with open(f"everybody_codes_e2024_q14_p{part}.txt") as f:
        return [[(m[0],int(m[1:])) for m in l.split(",")] for l in f.read().splitlines()]

def add_points(*points):
    return tuple(map(sum,zip(*points)))

def scale_point(point, scale):
    return tuple(map(scale.__mul__,point))

def create_mcfunction(filename, data, do_leaves = False):
    with open(filename, "w") as f:
        leaves = []
        for line in data:
            location = (0,0,0)
            for direction,length in line:
                y0,x0,z0 = add_points(location,direction_mapping[direction])
                y1,x1,z1 = location = add_points(location,scale_point(direction_mapping[direction],length))
                axis = axis_mapping[direction]
                print(f"fill ~{x0} ~{y0} ~{z0} ~{x1} ~{y1} ~{z1} minecraft:oak_log[{axis=}]",file=f)
            leaves.append(location)
        if do_leaves:
            for y1,x1,z1 in leaves:
                print(f"setblock ~{x1} ~{y1} ~{z1} minecraft:oak_leaves",file=f)

# U = +i, D = -i, L = -j, R = +j, F = +k
direction_mapping = {
    "U":(+1,0,0),
    "D":(-1,0,0),
    "R":(0,+1,0),
    "L":(0,-1,0),
    "F":(0,0,+1),
    "B":(0,0,-1),
}

axis_mapping = {
    "U":"y",
    "D":"y",
    "R":"x",
    "L":"x",
    "F":"z",
    "B":"z",
}

for part in (1,2,3):
    locations = set()
    leaves = []
    for line in load_file(part):
        location = (0,0,0)
        for direction,length in line:
            for _ in range(length):
                location = add_points(location,direction_mapping[direction])
                locations.add(location)
        leaves.append(location)
    if part == 1:
        print(max(locations)[0])
    elif part == 2:
        print(len(locations))

trunk = {(i,0,0) for i in range(max(locations)[0]+1) if (i,0,0) in locations}
location_costs = {leaf:{location:0 if location == leaf else 1e8 for location in locations} for leaf in leaves}
for leaf, costs in location_costs.items():
    to_update = locations
    while to_update:
        new_update = set()
        for loc in to_update:
            neighbours = [p for delta in direction_mapping.values() if (p:=add_points(loc,delta)) in costs]
            neighbour_costs = map(costs.get,neighbours)
            new_cost = min(neighbour_costs) + 1
            if new_cost < costs[loc]:
                costs[loc] = new_cost
                new_update.update(neighbours)
        to_update = new_update


def murkiness(tap_location):
    return sum(costs[tap_location] for costs in location_costs.values())

print(min(map(murkiness,trunk)))

# import matplotlib.pyplot as plt
# import numpy as np


# fig = plt.figure()
# ax = fig.add_subplot(projection='3d')
# # zs, xs, ys = zip(*(locations-set(leaves)-trunk))
# # ax.scatter(xs,ys,zs)
# zs, xs, ys = zip(*trunk)
# ax.scatter(xs,ys,zs,color="brown")
# zs, xs, ys = zip(*leaves)
# ax.scatter(xs,ys,zs,color="g")
# plt.show()

from pathlib import Path
datapack = Path(R"C:\Users\allan\AppData\Roaming\.minecraft\saves\Everybody Codes 2024\datapacks\autoec\data\q14\function")
create_mcfunction(datapack/"part1.mcfunction",load_file(1))
create_mcfunction(datapack/"part2.mcfunction",load_file(2))
create_mcfunction(datapack/"part3.mcfunction",load_file(3),True)
