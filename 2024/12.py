SEGMENT_NUMBER = {"A":1, "B":2, "C":3}

def load_file(part):
    with open(f"everybody_codes_e2024_q12_p{part}.txt") as f:
        return f.read().splitlines()

targets = set()
hard_targets = set()
catapults = {}
for i,line in enumerate(reversed(load_file(2))):
    for j,c in enumerate(line):
        if c == "T":
            targets.add((i,j))
        elif c == "H":
            hard_targets.add((i,j))
        elif c.isalpha():
            catapults[c] = (i,j)

def flight_path(catapult, power):
    i,j = catapults[catapult]
    path = []
    for _ in range(power):
        i += 1
        j += 1
        path.append((i,j))
    for _ in range(power):
        j += 1
        path.append((i,j))
    while i > 0:
        i -= 1
        j += 1
        path.append((i,j))
    return path

def plot(path=()):
    all_points = [*targets, *catapults.values(), *path]
    max_i = max(i for i,j in all_points)
    max_j = max(j for i,j in all_points)
    for i in range(max_i,0,-1):
        for j in range(max_j+1):
            point = "."
            if (i,j) in targets:
                point = "T"
            if (i,j) in hard_targets:
                point = "H"
            if (i,j) in catapults.values():
                point, = (k for k,v in catapults.items() if v == (i,j))
            if (i,j) in path:
                point = "*"
            print(end=point)
        print()
    print("="*(max_j+1))

def all_targets(path):
    return [p for p in path if p in targets or p in hard_targets]

def score(catapult, power, is_hard=False):
    return (ord(catapult)-64) * power * (2 if is_hard else 1)
assert score("B", 5) == 10

viable_shots = {}
for n in range(200):
    for catapult in catapults:
        path = flight_path(catapult, n)
        if ts := all_targets(path):
            viable_shots[catapult,n] = ts

hittable_locations = [p for v in viable_shots.values() for p in v]
assert len(hittable_locations) == len(set(hittable_locations))
print(sum(score(c,p,t in hard_targets) for (c,p),v in viable_shots.items() for t in v))
