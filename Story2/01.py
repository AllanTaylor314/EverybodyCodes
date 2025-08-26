from itertools import permutations

def load_file(part):
    with open(f"everybody_codes_e2_q01_p{part}.txt") as f:
        lines = f.read().splitlines()
    idx = lines.index("")
    return lines[:idx], lines[idx+1:]

def col_from_slot(slot):
    return (slot - 1) * 2

def slot_from_col(col):
    assert col % 2 == 0
    return col // 2 + 1

def score(grid, token, slot):
    row = 0
    col = col_from_slot(slot)
    directions = iter(token)
    while row < len(grid):
        if grid[row][col] == "*":
            col += 1 if next(directions) == "R" else -1
            if col == -1:
                col = 1
            elif col == len(grid[row]):
                col -= 2
        else:
            row += 1
    # print(slot, "=>", slot_from_col(col))
    return max((slot_from_col(col) * 2) - slot, 0)

total = 0
grid, tokens = load_file(1)
for i, token in enumerate(tokens, 1):
    s = score(grid, token, i)
    # print(s)
    total += s
print(total)

total = 0
grid, tokens = load_file(2)
for token in tokens:
    s = max(score(grid, token, i) for i in range(1,14))
    # print(s)
    total += s
print(total)

best = 0
worst = 10**10
grid, tokens = load_file(3)
scores = {}
for token in tokens:
    for slot in range(1,21):
        scores[token, slot] = score(grid, token, slot)
for slots in permutations(range(1,21), 6):
    total = sum(scores[token_slot] for token_slot in zip(tokens, slots))
    if total > best:
        best = total
    if total < worst:
        worst = total
print(worst, best)