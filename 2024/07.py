from itertools import cycle
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

with open("everybody_codes_e2024_q07_p2.txt") as f:
    lines = f.read().splitlines()
tracks.clear()
for line in lines:
    k,*v = line.replace(":",",").split(",")
    tracks[k] = v

def apply_track(plan):
    return "".join(b if a == '=' else a for a,b in zip(track*10, cycle(plan)))

soln = "".join(sorted(tracks, reverse=True, key=lambda k:score(apply_track(tracks[k]))))
print(soln)
# Not CIBKEGDHF (correct len and first char)
for k in soln:
    print(k, score(apply_track(tracks[k])))
