import re
import z3
from itertools import batched

PLOT = True

BLOCK_CHARS = " █"

HEADER = re.compile(r"^Plant (\d+) with thickness (-?\d+):$")
FREE_ROW = re.compile(r"- free branch with thickness (-?\d+)")
ROW = re.compile(r"^- branch to Plant (\d+) with thickness (-?\d+)$")
BITS = re.compile(r"^[01]\s")


def load_file(part):
    with open(f"everybody_codes_e2025_q18_p{part}.txt") as f:
        lines = f.read().splitlines()
    return lines


def to_tree(lines: list[str]):
    plants = {}
    for line in lines:
        if groups := HEADER.match(line):
            plant, thickness = map(int, groups.groups())
            latest_plant = plants[plant] = (thickness, [])
        elif groups := FREE_ROW.match(line):
            (thickness,) = map(int, groups.groups())
            latest_plant[1].append((None, thickness))
        elif groups := ROW.match(line):
            plant, thickness = map(int, groups.groups())
            latest_plant[1].append((plant, thickness))
    return plants


tree = to_tree(load_file(1))


def energy(branch):
    if branch is None:
        return 1
    thickness, branches = tree[branch]
    if branches[0][0] is None:
        return thickness
    incoming = sum(energy(p) * t for p, t in branches)
    if incoming >= thickness:
        return incoming
    return 0


print(energy(max(tree)))

lines = load_file(2)
tree = to_tree(lines)
bit_lists = [list(map(int, line.split())) for line in lines if BITS.match(line)]
last_plant = max(tree)
last_thickness = tree[last_plant][0]
free_branches = [
    branch
    for branch, (_, ((first_branch, _), *_)) in tree.items()
    if first_branch is None
]
total = 0
for bits in bit_lists:
    for branch, bit in zip(free_branches, bits):
        tree[branch] = (bit, [(None, bit)])
    e = energy(last_plant)
    if e >= last_thickness:
        total += e
print(total)
# Whoops - negatives weren't in regex


def zenergy(branch):
    if branch is None:
        return 1
    thickness, branches = tree[branch]
    if branches[0][0] is None:
        return thickness
    incoming = sum(zenergy(p) * t for p, t in branches)
    return z3.If(incoming < thickness, 0, incoming)


lines = load_file(3)
tree = to_tree(lines)
bit_lists = [list(map(int, line.split())) for line in lines if BITS.match(line)]
last_plant = max(tree)
last_thickness = tree[last_plant][0]
free_branches = [
    branch
    for branch, (_, ((first_branch, _), *_)) in tree.items()
    if first_branch is None
]

bits = [z3.Bool(f"b{i}") for i in free_branches]
for branch, bit in zip(free_branches, bits):
    tree[branch] = (bit, [(None, bit)])
e = zenergy(last_plant)
expr = z3.If(e < last_thickness, 0, e)

opt = z3.Optimize()
out_energy = z3.Int("out_energy")
opt.add(out_energy == expr)
h = opt.maximize(out_energy)
opt.check()
best = opt.upper(h).py_value()
best_model = opt.model()


def plot_bit_list(bit_list):
    for row in batched(bit_list, 9):
        print(*(BLOCK_CHARS[bit] * 2 for bit in row), sep="")


def plot_all_bit_lists(bit_lists, num_cols=10):
    row_sep = "+" + ("-" * 9 * 2 + "+") * num_cols
    print(row_sep)
    for bls in batched(bit_lists, num_cols):
        for groups in zip(*(batched(bl, 9) for bl in bls)):
            print(end="|")
            for row in groups:
                print(*(BLOCK_CHARS[bit] * 2 for bit in row), sep="", end="|")
            print()
        print(row_sep)


total = 0
for bit_list in bit_lists:
    s = z3.Solver()
    s.add(out_energy == expr, *(bit == bool(val) for bit, val in zip(bits, bit_list)))
    s.check()
    m = s.model()
    res = m[out_energy].py_value()
    if res:
        total += best - res
if PLOT:
    plot_all_bit_lists(bit_lists)
    plot_bit_list([best_model[b].py_value() for b in bits])
print(total)
