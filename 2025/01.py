def to_delta(s):
    d = s[0]
    n = int(s[1:])
    return -n if d == 'L' else n

def load_file(part):
    with open(f"everybody_codes_e2025_q01_p{part}.txt") as f:
        lines = f.read().splitlines()
    return lines
name_str,_,dir_str = load_file(1)
names = name_str.split(',')
dirs = dir_str.split(',')
i = 0
for d in dirs:
    delta = to_delta(d)
    i += delta
    if i < 0: i = 0
    if i >= len(names): i = len(names) - 1
print(names[i])

name_str,_,dir_str = load_file(2)
names = name_str.split(',')
dirs = dir_str.split(',')
i = 0
for d in dirs:
    delta = to_delta(d)
    i += delta
    i %= len(names)
print(names[i])

name_str,_,dir_str = load_file(3)
names = name_str.split(',')
dirs = dir_str.split(',')
for d in dirs:
    delta = to_delta(d) % len(names)
    names[0],names[delta] = names[delta],names[0]
print(names[0])