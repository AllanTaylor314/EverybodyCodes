from ast import literal_eval

def load_file(part):
    with open(f"everybody_codes_e2025_q02_p{part}.txt") as f:
        line, = f.read().splitlines()
    return literal_eval(line.split('=')[1])

def add(cn1,cn2):
    X1,Y1 = cn1
    X2,Y2 = cn2
    return [X1 + X2, Y1 + Y2]
def mul(cn1,cn2):
    X1,Y1 = cn1
    X2,Y2 = cn2
    return [X1 * X2 - Y1 * Y2, X1 * Y2 + Y1 * X2]
def div(cn1,cn2):
    X1,Y1 = cn1
    X2,Y2 = cn2
    return [int(X1 / X2), int(Y1 / Y2)]

num = load_file(1)
res = [0,0]
for _ in range(3):
    res = mul(res,res)
    res = div(res,[10,10])
    res = add(res,num)
print(str(res).replace(' ',''))

def test_point(point):
    res = [0,0]
    for _ in range(100):
        res = mul(res,res)
        res = div(res,[100000,100000])
        res = add(res,point)
        if -1000000 <= res[0] <= 1000000 >= res[1] >= -1000000:
            continue
        return False
    return True

top_left = load_file(2)
# top_left = [35300,-64910]
bottom_right = add(top_left, [1000,1000])
count = 0
lx,ty = top_left
rx,by = bottom_right
for y in range(ty,by+1,10):
    for x in range(lx,rx+1,10):
        if test_point([x,y]):
            count += 1
            print(end='X')
        else:
            print(end='.')
    print()
print(count)

top_left = load_file(3)
# top_left = [35300,-64910]
bottom_right = add(top_left, [1000,1000])
count = 0
lx,ty = top_left
rx,by = bottom_right
with open('2.egg.txt','w') as f:
    for y in range(ty,by+1,1):
        for x in range(lx,rx+1,1):
            if test_point([x,y]):
                count += 1
                print(end='x',file=f)
            else:
                print(end='·',file=f)
        print(file=f,flush=True)
print(count)