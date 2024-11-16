from collections import deque, Counter
from string import ascii_uppercase
with open(f"everybody_codes_e2024_q10_p1.txt") as f:
    lines = f.read().splitlines()
rows = [set(line)-{"."} for line in lines[2:6]]
cols = [set(line)-{"."} for line in list(zip(*lines))[2:6]]
for row in rows:
    for col in cols:
        print(*(row&col),end="")
print()

with open(f"everybody_codes_e2024_q10_p2.txt") as f:
    lines = f.read().splitlines()
big_rows = [lines[i:i+8] for i in range(0,len(lines),9)]
big_row = list(map(" ".join,zip(*big_rows)))
big_row = [l.split() for l in big_row]
grids = list(zip(*big_row))
words = []
for grid in grids:
    rows = [set(line)-{"."} for line in grid[2:6]]
    cols = [set(line)-{"."} for line in list(zip(*grid))[2:6]]
    word = ""
    for row in rows:
        for col in cols:
            word += (row&col).pop()
    words.append(word)

def score(word):
    if "." in word:
        return 0
    return sum(i*(ord(c)-64) for i,c in enumerate(word,1))

assert score("PTBVRCZHFLJWGMNS") == 1851

print(sum(map(score,words)))

with open(f"everybody_codes_e2024_q10_p3.txt") as f:
    wall = list(map(list,f.read().splitlines()))

def rc_index(row,col):
    srow = row//6*6
    scol = col//6*6
    assert 1 < row%6
    assert 1 < col%6
    return [(row,scol+n) for n in [0,1,6,7]],[(srow+n,col) for n in [0,1,6,7]]

def rc_index2(row,col):
    srow = row//6*6
    scol = col//6*6
    assert 1 < row%6
    assert 1 < col%6
    return [(row,scol+n) for n in [2,3,4,5]],[(srow+n,col) for n in [2,3,4,5]]

def containing_regions(row,col):
    srow = row//6*6
    scol = col//6*6
    rs = range(srow,srow+8),range(srow-6,srow+2)
    cs = range(scol,scol+8),range(scol-6,scol+2)
    return [(r,c) for r in rs for c in cs if (row in r and col in c and r[0]>=0 and r[-1]<len(wall) and c[0]>=0 and c[-1]<len(wall[0]))]

# Validate regions
for i,row in enumerate(wall):
    for j,c in enumerate(row):
        for rs,cs in containing_regions(i,j):
            [wall[r][c] for r in rs for c in cs]
            assert i in rs
            assert j in cs

def rc_index_region(region):
    rows, cols = map(list,region)
    row_indices = [(i,j) for i in rows[2:6] for j in cols[:2]+cols[-2:]]
    col_indices = [(i,j) for i in rows[:2]+rows[-2:] for j in cols[2:6]]
    return row_indices, col_indices

def rc_index2_region(region):
    rows, cols = region
    return [(i,j) for i in rows[2:6] for j in cols[2:6]]

runic_starts = [(i,j) for i in range(2,len(wall),6) for j in range(2,len(wall[0]),6)]
question_marks = {(i,j):set(ascii_uppercase) for i,line in enumerate(wall) for j,c in enumerate(line) if c=="?"}
# ~ For each question mark, if it's the only question mark in its region, give it the remaining letter
for i,j in question_marks:
    regions = containing_regions(i,j)
    for region in regions:
        ri,ci = rc_index_region(region)
        row_letters = [wall[i][j] for i,j in ri]
        col_letters = [wall[i][j] for i,j in ci]
        rq = "?" in row_letters
        cq = "?" in col_letters
        solvable = True
        if rq and cq:
            # Might be solvable...
            row_copy = row_letters.copy()
            col_copy = col_letters.copy()
            for c in row_copy:
                if c != "?":
                    try:
                        col_letters.remove(c)
                    except ValueError:
                        solvable = False
            for c in col_copy:
                if c != "?":
                    try:
                        row_letters.remove(c)
                    except ValueError:
                        solvable = False
        elif rq:
            for c in row_letters.copy():
                if c != "?":
                    try:
                        col_letters.remove(c)
                        row_letters.remove(c)
                    except ValueError:
                        solvable = False
            if solvable:
                question_marks[i,j] &= set(col_letters)
        elif cq:
            for c in col_letters.copy():
                if c != "?":
                    try:
                        row_letters.remove(c)
                        col_letters.remove(c)
                    except ValueError:
                        solvable = False
            if solvable:
                question_marks[i,j] &= set(row_letters)
        if not solvable:
            for m,n in rc_index2_region(region):
                wall[m][n] = "@" # Ignore the region
        print(row_letters, col_letters, solvable)
        # input()



def read_rune(row,col):
    return "".join(wall[row+i][col+j] for i in range(4) for j in range(4))

q = deque([(i,j) for i,line in enumerate(wall) for j,c in enumerate(line) if c=="."])
q.append(None)
changed = True
while q:
    top = q.popleft()
    if top is None:
        if changed:
            q.append(None)
            changed = False
            continue
        break
    r,c = top
    row_indices, col_indices = rc_index(r,c)
    row_letters = set(wall[i][j] for i,j in row_indices)
    col_letters = set(wall[i][j] for i,j in col_indices)
    row_indices2, col_indices2 = rc_index2(r,c)
    used_row_letters = set(wall[i][j] for i,j in row_indices2)
    used_col_letters = set(wall[i][j] for i,j in col_indices2)
    remaining_row = row_letters - used_row_letters
    remaining_col = col_letters - used_col_letters
    try:
        wall[r][c] ,= remaining_row & remaining_col - {"?"}
        changed = True
    except ValueError: # Not solvable?
        if "?" in row_letters|col_letters:
            # print(r,c,row_letters,col_letters)
            print(f"{r,c}: {remaining_row}, {remaining_col}")
            if "?" not in remaining_row and len(remaining_row) == 1:
                wall[r][c] ,= remaining_row
                try:
                    (qr,qc) ,= ((i,j) for i,j in col_indices if wall[i][j] == "?")
                except ValueError:
                    q.append((r,c))
                else:
                    wall[qr][qc] = wall[r][c]
                changed = True
            elif "?" not in remaining_col and len(remaining_col) == 1:
                wall[r][c] ,= remaining_col
                try:
                    (qr,qc) ,= ((i,j) for i,j in row_indices if wall[i][j] == "?")
                except ValueError:
                    q.append((r,c))
                else:
                    wall[qr][qc] = wall[r][c]
                changed = True
            else:
                q.append((r,c))
    

for line in wall:
    print(*line,sep="")
print(sum(map(score,(read_rune(r,c) for r,c in runic_starts))))
