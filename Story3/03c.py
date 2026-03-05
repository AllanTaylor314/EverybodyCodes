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

PART = 3

def strong_match(a,b):
    return a == b

def weak_match(a,b):
    color_a, shape_a = a.split()
    color_b, shape_b = b.split()
    return color_a == color_b or shape_a == shape_b

def strict_weak_match(a,b):
    color_a, shape_a = a.split()
    color_b, shape_b = b.split()
    return (color_a == color_b) != (shape_a == shape_b)

data = list(map(parse_line,load_file(PART)))
lut = {d['id']:d for d in data}

root = data[0]

def link_node(tree, new_node):
    left = tree.get('left')
    if left is None:
        if weak_match(new_node['plug'], tree['leftSocket']):
            tree['left'] = new_node['id']
            return None
    elif strict_weak_match(lut[left]['plug'], tree['leftSocket']) and strong_match(new_node['plug'], tree['leftSocket']):
        tree['left'] = new_node['id']
        new_node = lut[left]
    else:
        new_node = link_node(lut[left], new_node)

    if new_node is None:
        return None

    right = tree.get('right')
    if right is None:
        if weak_match(new_node['plug'], tree['rightSocket']):
            tree['right'] = new_node['id']
            return None
    elif strict_weak_match(lut[right]['plug'], tree['rightSocket']) and strong_match(new_node['plug'], tree['rightSocket']):
        tree['right'] = new_node['id']
        new_node = lut[right]
    else:
        new_node = link_node(lut[right], new_node)
    return new_node

for node in data[1:]:
    while node:
        node = link_node(root, node)

order = iot(root)
print(sum(i*int(j) for i,j in enumerate(order, start=1)))