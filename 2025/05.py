def score(nums, include_levels=False):
    spine = []
    quality = 0
    for num in nums:
        for vertibra in spine:
            if num < vertibra[1] and vertibra[0] is None:
                vertibra[0] = num
                break
            elif num > vertibra[1] and vertibra[2] is None:
                vertibra[2] = num
                break
        else:
            spine.append([None, num, None])
            quality = quality * 10 + num
    if not include_levels:
        return quality
    levels = []
    for vertibra in spine:
        r = 0
        for n in vertibra:
            if n is not None:
                r = r * 10 + n
        levels.append(r)
    return quality, levels


def parse_line(line):
    id, nums = line.split(":")
    nums = list(map(int, nums.split(",")))
    return int(id), nums


def load_file(part):
    with open(f"everybody_codes_e2025_q05_p{part}.txt") as f:
        lines = f.read().splitlines()
    return list(map(parse_line, lines))


print(score(load_file(1)[0][1]))

scores = [score(n) for _, n in load_file(2)]
print(max(scores) - min(scores))

scores = [(score(n, True), i) for i, n in load_file(3)]
scores.sort(reverse=True)
print(sum(idx * i for idx, (_, i) in enumerate(scores, 1)))
