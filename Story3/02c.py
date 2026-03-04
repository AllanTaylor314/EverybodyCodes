from time import perf_counter

t0 = perf_counter()

def load_file(part):
    with open(f"everybody_codes_e3_q02_p{part}.txt") as f:
        return f.read().splitlines()


# for i, line in enumerate(load_file(1)):
#     for j, c in enumerate(line):
#         if c == '@':
#             start = i,j
#         if c == '#':
#             end = i,j


# step_index = 0
def step(p):
    global step_index
    i, j = p
    s = step_index % 4
    step_index += 1
    if s == 0:
        return i - 1, j
    if s == 1:
        return i, j + 1
    if s == 2:
        return i + 1, j
    if s == 3:
        return i, j - 1


# pos = start
# seen = {pos}
# num_steps = 0
# while pos != end:
#     new = step(pos)
#     if new not in seen:
#         pos = new
#         num_steps += 1
#         seen.add(pos)
# print(num_steps)


###############################


def viz():
    for i, line in enumerate(data):
        for j, c in enumerate(line):
            if c == '#':
                print(end="#")
            elif (i, j) == pos:
                print(end="@")
            elif (i, j) in seen:
                print(end="+")
            else:
                print(end=".")
        print()


# for i, line in enumerate(load_file(2)):
#     for j, c in enumerate(line):
#         if c == "@":
#             start = i, j
#         if c == "#":
#             end = i, j


def all_adjs(p):
    i, j = p
    return [(i - 1, j), (i, j + 1), (i + 1, j), (i, j - 1)]

def is_enclosed(p):
    return not set(all_adjs(p)) - seen

def block_enclosed(p):
    for a in all_adjs(p):
        if a not in seen and is_enclosed(a):
            seen.add(a)
            block_enclosed(a)

# step_index = 0

# pos = start
# seen = {pos, end}
# goal = set(all_adjs(end))
# step_index = 0
# num_steps = 0
# while goal - seen:
#     new = step(pos)
#     if new not in seen:
#         pos = new
#         num_steps += 1
#         seen.add(pos)
#         block_enclosed(pos)
#         # viz()
#         # input(pos)
# print(num_steps)

###################################
bones = []
data = load_file(3)
for i, line in enumerate(data):
    for j, c in enumerate(line):
        if c == "@":
            start = i, j
        if c == "#":
            bones.append((i, j))

def flood_block():
    global seen
    min_i = min(i for i,j in seen) - 1
    max_i = max(i for i,j in seen) + 1
    min_j = min(j for i,j in seen) - 1
    max_j = max(j for i,j in seen) + 1
    changes = True
    reachable = {(min_i,j) for j in range(min_j,max_j+1)} | {(max_i,j) for j in range(min_j,max_j+1)} | {(i,min_j) for i in range(min_i,max_i+1)} | {(i,max_j) for i in range(min_i,max_i+1)}
    all_cells = {(i,j) for i in range(min_i,max_i+1) for j in range(min_j,max_j+1)}
    while changes:
        changes = False
        # for i in range(min_i, max_i + 1):
        #     for j in range(min_j, max_j + 1):
        #         if (i,j) in reachable and (i,j) not in seen:
        for (i,j) in list(reachable):
            if min_i <= i <= max_i and min_j <= j <= max_j and (i,j) not in seen:
                    l = len(reachable)
                    reachable.update(all_adjs((i,j)))
                    if len(reachable) > l:
                        changes = True
    seen |= all_cells - reachable
    


step_index = 0
def step(p):
    global step_index
    i, j = p
    s = (step_index//3) % 4
    step_index += 1
    if s == 0:
        return i - 1, j
    if s == 1:
        return i, j + 1
    if s == 2:
        return i + 1, j
    if s == 3:
        return i, j - 1

pos = start
seen = {pos, *bones}
goal = {a for bone in bones for a in all_adjs(bone)}
step_index = 0
num_steps = 0
fails = 0
flood_block()
while goal - seen:
    new = step(pos)
    if new not in seen:
        fails = 0
        pos = new
        num_steps += 1
        seen.add(pos)
        # block_enclosed(pos)
        flood_block()
        # viz()
        # input(pos)
        # print(num_steps)
    else:
        fails += 1
        if fails > 10:
            viz()
            raise ValueError("Trapped")
print(num_steps)
print(perf_counter() - t0)