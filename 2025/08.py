from itertools import pairwise
import matplotlib.pyplot as plt
import numpy as np

def plot(nails,num_points,part):
    ax = plt.axes()
    ts = np.linspace(0,2*np.pi,num_points+1)[:-1]
    xs = np.sin(ts)
    ys = np.cos(ts)
    ns = np.array(nails) - 1
    ax.plot(xs[ns],ys[ns],lw=0.02)
    ax.set_aspect(1)
    ax.set_axis_off()
    plt.savefig(f'08.{part}.egg.png')


def load_file(part):
    with open(f"everybody_codes_e2025_q08_p{part}.txt") as f:
        return list(map(int,f.read().strip().split(',')))

nums = load_file(1)
plot(nums, 32, 1)
total_centre_crossings = 0
for a,b in pairwise(nums):
    if abs(a-b) == 16: # 32//2
        total_centre_crossings+=1
print(total_centre_crossings)

nums = load_file(2)
plot(nums, 256, 2)
total_knots = 0
pairs = []
for a,b in pairwise(nums):
    if b < a: a,b=b,a
    pair = a,b
    for c,d in pairs:
        if a < c < b < d or c < a < d < b:
            total_knots += 1
    pairs.append(pair)
print(total_knots)

nums = load_file(3)
plot(nums, 256, 3)
pairs = []
for a,b in pairwise(nums):
    if b < a: a,b=b,a
    pair = a,b
    pairs.append(pair)

counts = {}
for a in range(1,257):
    for b in range(a+1,257):
        count = 0
        for c,d in pairs:
            if a < c < b < d or c < a < d < b or (a == c and b == d):
                count += 1
        counts[a,b] = count
print(max(counts.values()))