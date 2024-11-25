from itertools import zip_longest

def load_file(part):
    with open(f"everybody_codes_e2024_q16_p{part}.txt") as f:
        header, _, *remainder = f.read().splitlines()
    wheel_distances = list(map(int,header.split(",")))
    wheels_transpose = [[line[i:i+3].strip() for i in range(0,len(line),4)] for line in remainder]
    wheels = [list(filter(None,wheel)) for wheel in zip_longest(*wheels_transpose,fillvalue="")]
    return wheel_distances, wheels

wheel_distances, wheels = load_file(1)
wheel_positions = [0] * len(wheel_distances)
# wheel_positions = list(map(sum,zip(wheel_positions,wheel_distances)))
wheel_positions = [(a+b)*100%len(c) for a,b,c in zip(wheel_positions,wheel_distances,wheels)]

print(*(wheel[i] for i,wheel in zip(wheel_positions,wheels)))

# Not <,- <:> -,* <,^ (correct first char and len)
# It was <,- <.< *,- <,^ (which is the result of 100 spins, not one more spin)
