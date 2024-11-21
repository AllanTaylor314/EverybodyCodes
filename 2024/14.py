def load_file(part):
    with open(f"everybody_codes_e2024_q14_p{part}.txt") as f:
        return f.read().split(",")

moves = load_file(1)
height = 0
heights = []
for move in moves:
    if move[0] == "U":
        height += int(move[1:])
    elif move[0] == "D":
        height -= int(move[1:])
    heights.append(height)
print(max(heights))
