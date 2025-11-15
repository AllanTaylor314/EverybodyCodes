from collections import deque
from functools import cache


def dragon_moves(position):
    i,j = position
    yield i+1,j+2
    yield i+1,j-2
    yield i-1,j+2
    yield i-1,j-2
    
    yield i+2,j+1
    yield i+2,j-1
    yield i-2,j+1
    yield i-2,j-1

def in_grid(pos,grid):
    i,j = pos
    return 0 <= i < len(grid) and 0 <= j < len(grid[0])

def load_file(part):
    with open(f"everybody_codes_e2025_q10_p{part}.txt") as f:
        lines = f.read().splitlines()
    return lines

grid = load_file(1)
sheep = set()
for i,row in enumerate(grid):
    for j,c in enumerate(row):
        if c == 'D':
            start = i,j
        if c == 'S':
            sheep.add((i,j))

dragons = {start}
for _ in range(4):
    dragons |= {d for p in dragons for d in dragon_moves(p) if in_grid(d,grid)}
print(len(sheep&dragons)) # not 157, 91


grid = load_file(2)
sheep = set()
havens = set()
for i,row in enumerate(grid):
    for j,c in enumerate(row):
        if c == 'D':
            start = i,j
        if c == 'S':
            sheep.add((i,j))
        if c == '#':
            havens.add((i,j))

dragons = {start}
eaten = 0
for _ in range(20):
    # Dragon turn
    dragons = {d for p in dragons for d in dragon_moves(p) if in_grid(d,grid)}
    to_be_eaten = dragons & sheep - havens
    eaten += len(to_be_eaten)
    sheep -= to_be_eaten
    # Sheep turn
    sheep = {(i+1,j) for i,j in sheep if i + 1 < len(grid)}
    to_be_eaten = dragons & sheep - havens
    eaten += len(to_be_eaten)
    sheep -= to_be_eaten
print(eaten)

def sheep_turns(dragon,sheep):
    move_made = False
    for pos in sheep:
        i,j = pos
        new_pos = i+1,j
        if new_pos != dragon or new_pos in havens:
            new_sheep = set(sheep)
            new_sheep.remove(pos)
            if i + 1 < len(grid):
                new_sheep.add(new_pos)
                yield frozenset(new_sheep) # Only yield games that can be won
            move_made = True
    if not move_made:
        yield sheep

def dragon_turns(dragon,sheep):
    for new_pos in dragon_moves(dragon):
        if in_grid(new_pos,grid):
            new_sheep = set(sheep)
            if new_pos not in havens:
                new_sheep.discard(new_pos)
            yield new_pos,frozenset(new_sheep)


grid = load_file(3)
sheep = set()
havens = set()
for i,row in enumerate(grid):
    for j,c in enumerate(row):
        if c == 'D':
            dragon = i,j
        if c == 'S':
            sheep.add((i,j))
        if c == '#':
            havens.add((i,j))

# q = deque([(0,'D',dragon,frozenset(sheep))])
# num_wins = 0
# # seen_states = set() # Doesn't seem to work :(
# while q:
#     turn, player, dragon, sheep = q.popleft()
#     # if (player,dragon,sheep) in seen_states: continue
#     # seen_states.add((player,dragon,sheep))
#     if player == 'D':
#         for d,s in dragon_turns(dragon,sheep):
#             if not s:
#                 num_wins += 1
#                 print(num_wins,len(q))
#             else:
#                 q.append((turn,'S',d,s))
#     else:
#         for s in sheep_turns(dragon, sheep):
#             q.append((turn+1,'D',dragon,s))
# print(num_wins)

@cache
def num_winning_games(player,dragon,sheep):
    num_wins = 0
    if player == 'D':
        for d,s in dragon_turns(dragon,sheep):
            if not s:
                num_wins += 1
            else:
                num_wins += num_winning_games('S',d,s)
    else:
        for s in sheep_turns(dragon, sheep):
            num_wins += num_winning_games('D',dragon,s)
    return num_wins
print(num_winning_games('S',dragon,frozenset(sheep)))