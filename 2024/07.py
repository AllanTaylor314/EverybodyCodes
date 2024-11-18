from itertools import cycle, permutations
DELTAS = {"+":1,"-":-1,"=":0}

P2_TRACK = """
S-=++=-==++=++=-=+=-=+=+=--=-=++=-==++=-+=-=+=-=+=+=++=-+==++=++=-=-=--
-                                                                     -
=                                                                     =
+                                                                     +
=                                                                     +
+                                                                     =
=                                                                     =
-                                                                     -
--==++++==+=+++-=+=-=+=-+-=+-=+-=+=-=+=--=+++=++=+++==++==--=+=++==+++-
""".strip()

P3_TRACK = """
S+= +=-== +=++=     =+=+=--=    =-= ++=     +=-  =+=++=-+==+ =++=-=-=--
- + +   + =   =     =      =   == = - -     - =  =         =-=        -
= + + +-- =-= ==-==-= --++ +  == == = +     - =  =    ==++=    =++=-=++
+ + + =     +         =  + + == == ++ =     = =  ==   =   = =++=
= = + + +== +==     =++ == =+=  =  +  +==-=++ =   =++ --= + =
+ ==- = + =   = =+= =   =       ++--          +     =   = = =--= ==++==
=     ==- ==+-- = = = ++= +=--      ==+ ==--= +--+=-= ==- ==   =+=    =
-               = = = =   +  +  ==+ = = +   =        ++    =          -
-               = + + =   +  -  = + = = +   =        +     =          -
--==++++==+=+++-= =-= =-+-=  =+-= =-= =--   +=++=+++==     -=+=++==+++-
""".strip()

def load_file(part):
    with open(f"everybody_codes_e2024_q07_p{part}.txt") as f:
        lines = f.read().splitlines()
    tracks = {}
    for line in lines:
        k,*v = line.replace(":",",").split(",")
        tracks[k] = v
    return tracks

def score(vals):
    current = 10
    total = 0
    for val in vals:
        current = max(0, current + DELTAS[val])
        total += current
    return total

def parse_track(track_2d):
    track_grid = {}
    for i,line in enumerate(track_2d.splitlines()):
        for j,c in enumerate(line):
            if c != " ":
                track_grid[complex(i,j)] = c

    directions = [1j**i for i in range(4)]
    path = [0j,1j]
    while path[-1]:
        current = path[-1]
        prev = path[-2]
        for d in directions:
            new = current + d
            if new == prev:
                continue
            if new in track_grid:
                path.append(new)
                break
    path.pop(0)
    track_grid[0] = "=" # Replace S
    return "".join(map(track_grid.get, path))

def apply_track(plan):
    return "".join(b if a == '=' else a for a,b in zip(track, cycle(plan)))

tracks = load_file(1)
track = "="*10
print("".join(sorted(tracks, reverse=True, key=lambda k:score(apply_track(tracks[k])))))


tracks = load_file(2)
track = parse_track(P2_TRACK) * 10
print("".join(sorted(tracks, reverse=True, key=lambda k:score(apply_track(tracks[k])))))

opps_plan ,= load_file(3).values()
track = parse_track(P3_TRACK) * 2024
score_to_beat = score(apply_track(opps_plan))
candidates = set(map("".join,permutations(opps_plan)))
soln3 = 0
for candidate in candidates:
    candidate_score = score(apply_track(candidate))
    if candidate_score > score_to_beat:
        soln3 += 1
print(soln3)
