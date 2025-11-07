def score(nums,include_levels=False):
    spine = []
    res = 0
    for num in nums:
        for ex in spine:
            if num < ex[1] and ex[0] is None:
                ex[0] = num
                break
            elif num > ex[1] and ex[2] is None:
                ex[2] = num
                break
        else:
            spine.append([None,num,None])
            res = res * 10 + num
    if not include_levels:
        return res
    levels = []
    for p in spine:
        r = 0
        for n in p:
            if n is None:
                continue
            r = r * 10 + n
        levels.append(r)
    return res, levels

def parse_line(line):
    id,nums = line.split(':')
    nums = list(map(int,nums.split(',')))
    return int(id),nums


def load_file(part):
    with open(f"everybody_codes_e2025_q05_p{part}.txt") as f:
        lines = f.read().splitlines()
    return lines

(_,nums) = load_file(1)[0].split(':')
nums = list(map(int,nums.split(',')))
print(score(nums))

p2 = load_file(2)
idn = [parse_line(line) for line in p2]
scores = [score(n) for _,n in idn]
print(max(scores)-min(scores))

p3 = load_file(3)
idn = [parse_line(line) for line in p3]
scores = [(score(n,True),i) for i,n in idn]
scores.sort(reverse=True)
ids = [s[1] for s in scores]
cs = sum(i*n for i,n in enumerate(ids,1))
print(cs)