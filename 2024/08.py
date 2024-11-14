from itertools import count
with open(f"everybody_codes_e2024_q08_p1.txt") as f:
    data = int(f.read())

     #     1
    ###    4
   #####   9
  ####### 16

total = 0
for width in count(start=1,step=2):
    total += width
    if total >= data:
        break
missing = total - data
print(width * missing)
