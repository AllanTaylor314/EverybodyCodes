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

with open(f"everybody_codes_e2024_q08_p2.txt") as f:
    data = int(f.read())

np, npa, nb = data, 1111, 20240000
# np, npa, nb = 3, 5, 50

total = 0
thickness = 1
for width in count(1,2):
    total += thickness * width
    thickness = (thickness * np) % npa
    if total >= nb:
        break
missing = total - nb
print(missing * width)

with open(f"everybody_codes_e2024_q08_p3.txt") as f:
    data = int(f.read())

hp, hpa, nb = data, 10, 202400000
# hp, hpa, nb = 2,5,160

thickness = 1
total = 0
column_heights = []
for width in count(1,2):
    column_heights.append(0)
    column_heights = [ch + thickness for ch in column_heights]
    empty = [hp*width*ch%hpa for ch in column_heights]
    empty[-1] = 0
    remaining = [ch-ne for ch,ne in zip(column_heights,empty)]
    total = sum(remaining)*2 - remaining[0]
    thickness = (thickness * hp) % hpa + hpa
    if total >= nb:
        break
print(total - nb)
