from itertools import cycle
DELTAS = {"+":1,"-":-1,"=":0}

with open("everybody_codes_e2024_q07_p1.txt") as f:
    lines = f.read().splitlines()
def score(vals):
    current = 10
    total = 0
    for _,val in zip(range(10),cycle(vals)):
        current = max(0, current + DELTAS[val])
        total += current
    return total

tracks = {}
for line in lines:
    k,*v = line.replace(":",",").split(",")
    tracks[k] = v

soln = "".join(sorted(tracks, reverse=True, key=lambda k:score(tracks[k])))
print(soln)
for c in soln:
    print(c, score(tracks[c]))
