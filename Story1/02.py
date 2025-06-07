import re
from collections import defaultdict

class Node:
    NODES_BY_ID = defaultdict(list)
    def __init__(self, id, weight, letter, left=None, right=None):
        self.id = id
        self.weight = weight
        self.letter = letter
        self.left = left
        self.right = right
        self.NODES_BY_ID[id].append(self)

    def __repr__(self):
        return f"Node({self.id!r}, {self.weight!r}, {self.letter!r}{'' if self.left is None else f', left={self.left!r}'}{'' if self.right is None else f', right={self.right!r}'})"
    def __lt__(self, other: "Node"):
        return self.weight < other.weight
    
    @classmethod
    def swap_nodes(cls, id):
        nodes = cls.NODES_BY_ID[id][-2:] # Just the last 2
        l, r = nodes
        l.weight, r.weight = r.weight, l.weight
        l.letter, r.letter = r.letter, l.letter
    
    @classmethod
    def swap_branches(cls, id):
        nodes = cls.NODES_BY_ID[id][-2:] # Just the last 2
        l, r = nodes
        l.weight, r.weight = r.weight, l.weight
        l.letter, r.letter = r.letter, l.letter
        l.left, r.left = r.left, l.left
        l.right, r.right = r.right, l.right
    
    @classmethod
    def reset(cls):
        cls.NODES_BY_ID.clear()

class Tree:
    def __init__(self, root=None):
        self.root = root
    def add(self, node: Node):
        if self.root is None:
            self.root = node
            return
        root = self.root
        while True:
            if node < root:
                if root.left is None:
                    root.left = node
                    return
                root = root.left
            else:
                if root.right is None:
                    root.right = node
                    return
                root = root.right
    def __repr__(self):
        return f"Tree({self.root!r})"
    def at_depth(self, n):
        return "".join(self._nodes_depth(self.root, n))
    @staticmethod
    def _nodes_depth(node, depth):
        if node is None: return
        if depth < 0: return
        if depth > 0:
            yield from Tree._nodes_depth(node.left, depth - 1)
            yield from Tree._nodes_depth(node.right, depth - 1)
        else:
            yield node.letter

def load_file(part):
    with open(f"everybody_codes_e1_q02_p{part}.txt") as f:
        return f.read().splitlines()

def parse_add_line(line):
    return re.match(r"ADD id=(\d+) left=\[(\d+),(.*)\] right=\[(\d+),(.*)\]", line).groups()

def parse_swap_line(line):
    return line.replace("SWAP ","")

# PART 1
Node.reset()
lines = load_file(1)
left_tree = Tree()
right_tree = Tree()

for line in lines:
    id, lw,lc,rw,rc = parse_add_line(line)
    left_tree.add(Node(int(id), int(lw), lc))
    right_tree.add(Node(int(id), int(rw), rc))

print(max((left_tree.at_depth(i) for i in range(10)), key = len)+max((right_tree.at_depth(i) for i in range(10)), key = len))


# PART 2
lines = load_file(2)
left_tree = Tree()
right_tree = Tree()

for line in lines:
    if line.startswith("ADD"):
        id, lw,lc,rw,rc = parse_add_line(line)
        left_tree.add(Node(int(id), int(lw), lc))
        right_tree.add(Node(int(id), int(rw), rc))
    elif line.startswith("SWAP"):
        Node.swap_nodes(int(parse_swap_line(line)))

print(max((left_tree.at_depth(i) for i in range(10)), key = len)+max((right_tree.at_depth(i) for i in range(10)), key = len))

# PART 3
lines = load_file(3)
left_tree = Tree()
right_tree = Tree()

for line in lines:
    if line.startswith("ADD"):
        id, lw,lc,rw,rc = parse_add_line(line)
        left_tree.add(Node(int(id), int(lw), lc))
        right_tree.add(Node(int(id), int(rw), rc))
    elif line.startswith("SWAP"):
        Node.swap_branches(int(parse_swap_line(line)))

print(max((left_tree.at_depth(i) for i in range(10)), key = len)+max((right_tree.at_depth(i) for i in range(10)), key = len))
