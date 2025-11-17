from itertools import count


def load_file(part):
    with open(f"everybody_codes_e2025_q11_p{part}.txt") as f:
        lines = f.read().splitlines()
    return list(map(int, lines))


def phase1(ducks):
    changed = False
    for i in range(len(ducks) - 1):
        if ducks[i] > ducks[i + 1]:
            ducks[i + 1] += 1
            ducks[i] -= 1
            changed = True
    return changed


def phase2(ducks):
    changed = False
    for i in range(len(ducks) - 1):
        if ducks[i] < ducks[i + 1]:
            ducks[i + 1] -= 1
            ducks[i] += 1
            changed = True
    return changed


def checksum(ducks):
    return sum(i * v for i, v in enumerate(ducks, 1))


def slow_solve(ducks):
    phase = True
    for n in count():
        if phase:
            phase = phase1(ducks)
            if not phase:
                print(f"Switched to phase 2 at {n} rounds")
        if not phase:
            if not phase2(ducks):
                break
    return n


def fast_solve(ducks):  # Given strictly ascending
    target = sum(ducks) // len(ducks)
    return sum(abs(d - target) for d in ducks) // 2


ducks = load_file(1)
changed = True
phase = True
for _ in range(10):
    if phase:
        phase = phase1(ducks)
    if not phase:
        phase2(ducks)
print(checksum(ducks))

print(slow_solve(load_file(2)))
# print(fast_solve(load_file(2)))
# print(slow_solve(load_file(3)))
print(fast_solve(load_file(3)))

# Why is part 3 strictly ascending? I guess it makes it easier
