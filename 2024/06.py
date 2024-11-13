from collections import defaultdict, Counter

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
for part in [1,2,3]:
    with open(f"everybody_codes_e2024_q06_p{part}.txt") as f:
        lines = f.read().splitlines()
    adj_mat = defaultdict(list)
    for line in lines:
        par, *chdrn = line.replace(":",",").split(",")
        adj_mat[par] = chdrn
    paths = list(gen_paths(adj_mat,truncate=(None if part == 1 else 1)))
    lengths = Counter(map(len,paths))
    powerful_length, = (k for k,v in lengths.items() if v==1)
    print(*(path for path in paths if len(path) == powerful_length))

