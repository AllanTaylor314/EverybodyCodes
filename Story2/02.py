from itertools import count
from time import perf_counter
BOLTS = "RGB"

def load_file(part):
    with open(f"everybody_codes_e2_q02_p{part}.txt") as f:
        return f.read().strip()

balloons = load_file(1)
j = 0
for i in count():
    if j >= len(balloons):
        break
    bolt = BOLTS[i%len(BOLTS)]
    while j < len(balloons):
        if balloons[j] == bolt:
            j += 1
        else:
            j += 1
            break
print(i)

balloons = load_file(2) * 100
for i in count():
    if not balloons:
        break
    bolt = BOLTS[i%len(BOLTS)]
    if len(balloons) % 2 == 0 and balloons[0] == bolt:
        cut = len(balloons) // 2
        balloons = balloons[1:cut] + balloons[cut+1:]
    else:
        balloons = balloons[1:]
print(i)

class RepeatedString:
    def __init__(self, string, repeats):
        self.string = string
        self.repeats = repeats
    def __getitem__(self, index):
        return self.string[index % len(self.string)]
    def __len__(self):
        return len(self.string) * self.repeats
    def __repr__(self):
        return f"RepeatedString({self.string!r}, {self.repeats!r})"
    def __str__(self):
        return self.string * self.repeats

class SegmentTree:
    def __init__(self, values, start=0, end=None):
        if end is None:
            end = len(values)
        self.count = end - start
        self.is_leaf = self.count <= 1
        if self.is_leaf:
            if self.count:
                self.exists = True
                self.value = values[start]
            else:
                self.exists = False
        else:
            cut = start + (end-start) // 2
            self.left = SegmentTree(values, start, cut)
            self.right = SegmentTree(values, cut, end)
    def __len__(self):
        return self.count
    def __getitem__(self, index):
        if index >= self.count:
            raise IndexError("Index out of range")
        if self.is_leaf:
            if self.exists:
                return self.value
            raise IndexError("Deleted leaf")
        if index < self.left.count:
            return self.left[index]
        else:
            return self.right[index-self.left.count]
    def __delitem__(self, index):
        if index >= self.count:
            raise IndexError("Index out of range")
        if self.is_leaf:
            if self.exists:
                self.exists = False
                self.count = 0
            else:
                raise IndexError("Already deleted leaf")
        else:
            if index < self.left.count:
                del self.left[index]
            else:
                del self.right[index-self.left.count]
            self.count -= 1
            # Self-cleaning & discarding unused nodes
            if self.count <= 1:
                if self.count == 1:
                    self.value = self[0]
                self.is_leaf = True
                self.exists = True
                del self.left
                del self.right
            elif self.left.is_leaf:
                pass
            elif self.left.left.count == 0:
                self.left = self.left.right
            elif self.left.right.count == 0:
                self.left = self.left.left
            elif self.right.is_leaf:
                pass
            elif self.right.left.count == 0:
                self.right = self.right.right
            elif self.right.right.count == 0:
                self.right = self.right.left
    def __repr__(self):
        if self.is_leaf:
            return f"<ST>({self.value}, {self.exists})"
        return f"<ST({self.count})>[{self.left},{self.right}]"
def load_file(part):
    with open(f"everybody_codes_e2_q02_p{part}.txt") as f:
        return f.read().strip()

balloons = SegmentTree(RepeatedString(load_file(2), 100))
for i in count():
    if not balloons:
        break
    bolt = BOLTS[i%len(BOLTS)]
    if len(balloons) % 2 == 0 and balloons[0] == bolt:
        cut = len(balloons) // 2
        del balloons[cut]
    del balloons[0]
print(i)

start_time = perf_counter()
balloons = SegmentTree(RepeatedString(load_file(3), 100000))
print("Build:", perf_counter() - start_time)
for i in count():
    if i % 100000 == 0:
        print(i, len(balloons), perf_counter() - start_time, balloons.left.count, balloons.right.count)
    if not balloons:
        break
    bolt = BOLTS[i%len(BOLTS)]
    if len(balloons) % 2 == 0 and balloons[0] == bolt:
        cut = len(balloons) // 2
        del balloons[cut]
    del balloons[0]
print(i)
print(perf_counter() - start_time)