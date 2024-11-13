from itertools import cycle, permutations
DELTAS = {"+":1,"-":-1,"=":0}

with open("everybody_codes_e2024_q07_p1.txt") as f:
    lines = f.read().splitlines()
def score(vals):
    current = 10
    total = 0
    for val in vals:
        current = max(0, current + DELTAS[val])
        total += current
    return total

tracks = {}
for line in lines:
    k,*v = line.replace(":",",").split(",")
    tracks[k] = v

soln = "".join(sorted(tracks, reverse=True, key=lambda k:score(tracks[k])))
print(soln)

p2_track = """
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
top,*mids,bot = p2_track.splitlines()
left, right = map("".join, zip(*map(str.split, mids)))
track = top[1:]+right+bot[::-1]+left[::-1]+"="
track *= 10

with open("everybody_codes_e2024_q07_p2.txt") as f:
    lines = f.read().splitlines()
tracks.clear()
for line in lines:
    k,*v = line.replace(":",",").split(",")
    tracks[k] = v

def apply_track(plan):
    return "".join(b if a == '=' else a for a,b in zip(track, cycle(plan)))

soln = "".join(sorted(tracks, reverse=True, key=lambda k:score(apply_track(tracks[k]))))
print(soln)

p3_track = """
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

with open("everybody_codes_e2024_q07_p3.txt") as f:
    opps_plan = f.read().strip().split(":")[1].split(",")

track3 = {}
for i,line in enumerate(p3_track.splitlines()):
    for j,c in enumerate(line):
        if c != " ":
            track3[complex(i,j)] = c

directions = [1j**i for i in range(4)]
path = [0j,1j]
while path[-1]:
    current = path[-1]
    prev = path[-2]
    for d in directions:
        new = current + d
        if new == prev:
            continue
        if new in track3:
            path.append(new)
            break
path.pop(0)
track3[0] = "=" # Replace S
track = "".join(map(track3.get, path))
track *= 2024
score_to_beat = score(apply_track(opps_plan))
print(score_to_beat)
candidates = set(map("".join,permutations("+++++---===")))
print(len(candidates))
soln3 = 0
for candidate in candidates:
    candidate_score = score(apply_track(candidate))
    if candidate_score > score_to_beat:
        soln3 += 1
        print(candidate, candidate_score, soln3)
print(soln3)
