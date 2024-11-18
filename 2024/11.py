from collections import Counter
def load_file(part):
    with open(f"everybody_codes_e2024_q11_p{part}.txt") as f:
        lines = f.read().splitlines()
    tracks = {}
    for line in lines:
        k,*v = line.replace(":",",").split(",")
        tracks[k] = v
    return tracks

def counter_fromkeys(iterable, v):
    new = Counter()
    for k in iterable:
        new[k] += v
    return new

mapping = load_file(1)
counts = Counter("A")
for _ in range(4):
    new_counts = Counter()
    for k,v in counts.items():
        new_counts += counter_fromkeys(mapping[k],v)
    counts = new_counts
print(sum(counts.values()))

mapping = load_file(2)
counts = Counter("Z")
for _ in range(10):
    new_counts = Counter()
    for k,v in counts.items():
        new_counts += counter_fromkeys(mapping[k],v)
    counts = new_counts
print(sum(counts.values()))

mapping = load_file(3)
final_counts = []
for start in mapping:
    counts = Counter([start])
    for _ in range(20):
        new_counts = Counter()
        for k,v in counts.items():
            new_counts += counter_fromkeys(mapping[k],v)
        counts = new_counts
    final_counts.append(sum(counts.values()))
print(max(final_counts)-min(final_counts))
