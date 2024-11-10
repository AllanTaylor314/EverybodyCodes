for part in [1,2,3]:
    with open(f"everybody_codes_e2024_q4_p{part}.txt") as f:
        nums = list(map(int,f.read().splitlines()))
    print(min(sum(abs(num-target) for num in nums) for target in (range(min(nums),max(nums)+1) if part == 3 else [min(nums)])))
