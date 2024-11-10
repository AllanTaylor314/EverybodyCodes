with open("everybody_codes_e2024_q4_p1.txt") as f:
    nums = list(map(int,f.read().splitlines()))
print(sum(num-min(nums) for num in nums))

with open("everybody_codes_e2024_q4_p2.txt") as f:
    nums = list(map(int,f.read().splitlines()))
print(sum(num-min(nums) for num in nums))

with open("everybody_codes_e2024_q4_p3.txt") as f:
    nums = list(map(int,f.read().splitlines()))
print(min(sum(abs(t-num) for num in nums) for t in range(min(nums),max(nums)+1)))

# P3: not 239565640 (right len, wrong first dig)
# Ah, can hit or pull
