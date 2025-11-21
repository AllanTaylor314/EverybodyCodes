from itertools import count


def diags(p):
    i,j = p
    yield i+1,j+1
    yield i-1,j+1
    yield i+1,j-1
    yield i-1,j-1

def load_file(part):
    with open(f"everybody_codes_e2025_q14_p{part}.txt") as f:
        lines = f.read().splitlines()
    return lines

def new_state(p, states):
    n = sum(states.get(d,0) for d in diags(p))
    if states[p]:
        return n % 2 == 1
    return n % 2 == 0

grid = load_file(1)
states = {(r,c):cell=='#' for r,row in enumerate(grid) for c,cell in enumerate(row)}
total = 0
for _ in range(10):
    states = {p:new_state(p, states) for p in states}
    total += sum(states.values())
print(total)


grid = load_file(2)
states = {(r,c):cell=='#' for r,row in enumerate(grid) for c,cell in enumerate(row)}
total = 0
for _ in range(2025):
    states = {p:new_state(p, states) for p in states}
    total += sum(states.values())
print(total)

# IT'S A CHECKERBOARD - ONLY HALF THE THINGS DEPEND ON EACH OTHER!
def state_hash(states):
    n = 0
    for s in states.values():
        n = n*2 + s
    return n
def cycle_time(states): # ah, it won't necessarily get back to all empty
    seen_states = {}
    for c in count():
        hsh = state_hash(states)
        pc = seen_states.get(hsh)
        if pc is not None:
            return pc, c - pc
        seen_states[hsh] = c
        states = {p:new_state(p, states) for p in states}

def matching_states(states, target):
    seen_states = {}
    matches = {}
    for c in count():
        hsh = state_hash(states)
        pc = seen_states.get(hsh)
        if pc is not None:
            return pc, c - pc, matches
        if all(tv==states[tp] for tp,tv in target.items()):
            matches[c] = sum(states.values())
        seen_states[hsh] = c
        states = {p:new_state(p, states) for p in states}

grid = load_file(3)
target_states = {(r,c):cell=='#' for r,row in enumerate(grid) for c,cell in enumerate(row)}
states = {(i,j):False for i in range(-13,8+13) for j in range(-13,8+13)}
# print(cycle_time(states))

# even_states = {(i,j):False for i,j in states if i%2==j%2}
# print(cycle_time(even_states))
# odd_states = {(i,j):False for i,j in states if i%2!=j%2}
# print(cycle_time(odd_states)) # same, duh - it's a mirror image

cycle_start, cycle_size, matches = matching_states(states, target_states)
# Cycle start was 1 - not sure how that would affect things if it weren't
# Probably need to exclude any matches before it
num_reps, extra = divmod(1000000000, cycle_size)

print(sum(matches.values()) * num_reps + sum(v for k,v in matches.items() if k < extra))