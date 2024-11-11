from collections import defaultdict, Counter

with open("everybody_codes_e2024_q06_p1.txt") as f:
    lines = f.read().splitlines()

adj_mat = defaultdict(list)
for line in lines:
    par, *chdrn = line.replace(":",",").split(",")
    adj_mat[par] = chdrn

def gen_paths(matrix, root='RR', truncate=None, visited=None):
    if visited is None:
        visited = set()
    if root in visited: # Loop!
        return
    if root == "@":
        yield "@"
        return
    for subroot in matrix[root]:
        for path in gen_paths(matrix, subroot, truncate, visited|{root}):
            yield root[:truncate]+path

paths = list(gen_paths(adj_mat))
lengths = Counter(map(len,paths))
powerfull_length, = (k for k,v in lengths.items() if v==1)
print(*(path for path in paths if len(path) == powerfull_length))
# Not MKXCQTQFSR@ (argh - it'll be RRMKXCQTQFSR@)

with open("everybody_codes_e2024_q06_p2.txt") as f:
    lines = f.read().splitlines()
    adj_mat = defaultdict(list)
for line in lines:
    par, *chdrn = line.replace(":",",").split(",")
    adj_mat[par] = chdrn
paths = list(gen_paths(adj_mat,truncate=1))
lengths = Counter(map(len,paths))
powerfull_length, = (k for k,v in lengths.items() if v==1)
print(*(path for path in paths if len(path) == powerfull_length))
# Not RMXQQS@ (wrong length. Used part 1 text :fp:)

with open("everybody_codes_e2024_q06_p3.txt") as f:
    lines = f.read().splitlines()
    adj_mat = defaultdict(list)
for line in lines:
    par, *chdrn = line.replace(":",",").split(",")
    adj_mat[par] = chdrn
paths = list(gen_paths(adj_mat,truncate=1))
lengths = Counter(map(len,paths))
powerfull_length, = (k for k,v in lengths.items() if v==1)
print(*(path for path in paths if len(path) == powerfull_length))
