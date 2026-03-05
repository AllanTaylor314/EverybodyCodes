from pprint import pprint


def load_file(part):
    with open(f"everybody_codes_e3_q03_p{part}.txt") as f:
        return f.read().splitlines()

def parse_line(line: str):
    entries = line.split(', ')
    record = {}
    for entry in entries:
        k, v = entry.split('=')
        record[k] = v
    return record

PART = 2

def strong_match(a,b):
    return a == b

def weak_match(a,b):
    color_a, shape_a = a.split()
    color_b, shape_b = b.split()
    return color_a == color_b or shape_a == shape_b

data = list(map(parse_line,load_file(PART)))
lut = {d['id']:d for d in data}

print(data)

root = data[0]

def link_node(tree, new_node, matcher=strong_match):
    left = tree.get('left')
    if left is not None:
        if link_node(lut[left], new_node, matcher):
            return True
    else:
        if matcher(new_node['plug'], tree['leftSocket']):
            tree['left'] = new_node['id']
            return True
    right = tree.get('right')
    if right is not None:
        if link_node(lut[right], new_node, matcher):
            return True
    else:
        if matcher(new_node['plug'], tree['rightSocket']):
            tree['right'] = new_node['id']
            return True
    return False

for node in data[1:]:
    res = link_node(root, node, matcher=strong_match if PART == 1 else weak_match)
    assert res


pprint(data)

def iot(tree, out=None):
    if out is None:
        out = []
    left = tree.get('left')
    if left is not None:
        iot(lut[left], out)
    out.append(tree['id'])
    right = tree.get('right')
    if right is not None:
        iot(lut[right], out)
    return out

order = iot(root)
print(order)
print(sum(i*int(j) for i,j in enumerate(order, start=1)))