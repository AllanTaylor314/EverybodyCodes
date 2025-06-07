import re

def load_file(part):
    with open(f"everybody_codes_e1_q01_p{part}.txt") as f:
        return f.read().splitlines()

def parse_line(line):
    return list(map(int,re.findall(r"-?\d+", line)))

# PART 1
def eni(n, exp, mod):
    score = 1
    out = []
    for i in range(exp):
        score *= n
        score %= mod
        out.append(score)
    return int("".join(map(str, reversed(out))))

lines = list(map(parse_line, load_file(1)))

best = 0
for a,b,c,x,y,z,m in lines:
    total = eni(a, x, m) + eni(b, y, m) + eni(c, z, m)
    best = max(total, best)
print(best)

# PART 2
def eni5(n, exp, mod):
    exps = range(max(exp-4,0), exp+1)
    out = [pow(n, e, mod) for e in exps]
    return int("".join(map(str, reversed(out))))

lines = list(map(parse_line, load_file(2)))

best = 0
for a,b,c,x,y,z,m in lines:
    total = eni5(a, x, m) + eni5(b, y, m) + eni5(c, z, m)
    best = max(total, best)
print(best)

# PART 3
def enit(n, exp, mod):
    score = 1
    seen = set()
    scores = [score]
    while score not in seen:
        seen.add(score)
        score = score * n % mod
        scores.append(score)
    loop_start = scores.index(score)
    loop_end = len(scores) - 1
    loop_sum = sum(scores[loop_start+1:])
    loop_size = loop_end - loop_start
    # print(n, exp, mod,"sz", loop_size, "sm", loop_sum, "st", loop_start, "en", loop_end)
    # print(scores)
    reps, rexp = divmod(exp - loop_start, loop_size)
    # print(scores[:loop_start + 1], reps, '*', scores[loop_start+1:], scores[loop_start + 1:loop_start + 1 + rexp])
    return sum(scores[1:loop_start + 1]) + reps * loop_sum + sum(scores[loop_start + 1:loop_start + 1 + rexp])

lines = list(map(parse_line, load_file(3)))

best = 0
for a,b,c,x,y,z,m in lines:
    total = enit(a, x, m) + enit(b, y, m) + enit(c, z, m)
    best = max(total, best)
print(best)
