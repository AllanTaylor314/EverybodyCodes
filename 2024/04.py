for part in [1,2,3]:
    with open(f"everybody_codes_e2024_q4_p{part}.txt") as f:
        nums = list(map(int,f.read().splitlines()))
        if part == 3:
            nums.sort()
            target = nums[len(nums)//2]
        else:
            target = min(nums)
    print(sum(abs(num-target) for num in nums))
