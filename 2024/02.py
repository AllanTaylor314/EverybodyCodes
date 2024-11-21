with open("everybody_codes_e2024_q2_p1.txt") as f:
    top,_,text = f.read().splitlines()
words = top.split(":")[1].split(",")
print(sum(map(text.count,words)))

with open("everybody_codes_e2024_q2_p2.txt") as f:
    top,_,*lines = f.read().splitlines()
words = top.split(":")[1].split(",")
total = 0
text = " ".join(lines)
words.extend([w[::-1] for w in words])

def proc_line(line):
    locations = [False] * len(line)
    for i in range(len(line)):
        for word in words:
            l = len(word)
            if line[i:i+l] == word:
                locations[i:i+l] = [True]*l
    return sum(locations)
print(sum(map(proc_line,lines)))

with open("everybody_codes_e2024_q2_p3.txt") as f:
    top,_,*lines = f.read().splitlines()
words = top.split(":")[1].split(",")
words.extend([w[::-1] for w in words])
grid = [[False]*len(line) for line in lines]
for i,line in enumerate(lines):
    for j in range(len(line)):
        for word in words:
            l = len(word)
            if (line*2)[j:j+l] == word:
                for n in range(l):
                    grid[i][(j+n)%len(line)] = True
senil = list(map("".join,zip(*lines)))
for j,enil in enumerate(senil):
    for i in range(len(enil)):
        for word in words:
            l = len(word)
            if enil[i:i+l] == word:
                for n in range(l):
                    grid[i+n][j] = True
print(sum(map(sum,grid)))
