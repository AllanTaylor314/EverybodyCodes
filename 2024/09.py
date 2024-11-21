from functools import cache

with open(f"everybody_codes_e2024_q09_p1.txt") as f:
    numbers = list(map(int,f.read().splitlines()))
stamps = (10, 5, 3, 1)
beetles = 0
for num in numbers:
    for stamp in stamps:
        new_beetles, num = divmod(num, stamp)
        beetles += new_beetles
print(beetles)


with open(f"everybody_codes_e2024_q09_p2.txt") as f:
    numbers = list(map(int,f.read().splitlines()))
stamps = [1, 3, 5, 10, 15, 16, 20, 24, 25, 30]
stamps.reverse()

@cache
def num_beetles(brightness):
    if brightness == 0:
        return 0
    if brightness < 0:
        return 10**100
    best = 10**100
    for stamp in stamps:
        sub = num_beetles(brightness - stamp)
        best = min(best, 1 + sub)
    return best

print(sum(map(num_beetles,numbers)))

with open(f"everybody_codes_e2024_q09_p3.txt") as f:
    numbers = list(map(int,f.read().splitlines()))
stamps = [1, 3, 5, 10, 15, 16, 20, 24, 25, 30, 37, 38, 49, 50, 74, 75, 100, 101]
stamps.reverse()
num_beetles.cache_clear()

def two_balls(brightness):
    hb1 = brightness//2
    hb2 = brightness - hb1
    return min(num_beetles(hb1-i)+num_beetles(hb2+i) for i in range(51-brightness%2))

print(sum(map(two_balls,numbers)))
