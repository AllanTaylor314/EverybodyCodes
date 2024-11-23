def load_file(part):
    with open(f"everybody_codes_e2024_q15_p{part}.txt") as f:
        return {(i,j):c for i,row in enumerate(f.read().splitlines()) for j,c in enumerate(row) if c not in "#~"}

grid = load_file(3)
start = min(grid)

LETTERS = "ABCDEGHIJKNOPQR"
FLOWERS = [
    "allium",
    "azure_bluet",
    "blue_orchid",
    "cornflower",
    "red_tulip",
    "dandelion",
    "lilac",
    "lily_of_the_valley",
    "oxeye_daisy",
    "peony",
    "poppy",
    "rose_bush",
    "sunflower",
    "orange_tulip",
    "fern",
]
FLOWER_TEMPLATE = "setblock ~{{j}} ~ ~{{i}} minecraft:{}"
PATH_TEMPLATE = "setblock ~{j} ~-1 ~{i} minecraft:dirt_path"
PODZOL_TEMPLATE = "setblock ~{j} ~-1 ~{i} minecraft:podzol"
CHAR_TO_COMMAND = {
    "#":"fill ~{j} ~ ~{i} ~{j} ~1 ~{i} minecraft:cobblestone",
    "~":"setblock ~{j} ~-1 ~{i} minecraft:water",
    ".":"setblock ~{j} ~-1 ~{i} minecraft:grass_block",
}
for letter, flower in zip(LETTERS, FLOWERS):
    CHAR_TO_COMMAND[letter] = FLOWER_TEMPLATE.format(flower)


from pathlib import Path
datapack = Path(R"C:\Users\allan\AppData\Roaming\.minecraft\saves\Everybody Codes 2024\datapacks\autoec\data\q15\function")
filename = datapack/"part3.mcfunction"

with open(f"everybody_codes_e2024_q15_p3.txt") as f:
    lines = f.read().splitlines()
di,dj = start

herb_locations = set()
with open(filename,"w") as f:
    for i,line in enumerate(lines):
        for j,c in enumerate(line):
            print(CHAR_TO_COMMAND[c].format(j=i-di,i=j-dj),file=f)
            if c.isalpha():
                herb_locations.add((i,j))

with open(f"everybody_codes_e2024_q15_p3_path.txt") as fi, open(datapack/"part3path.mcfunction","w") as fo:
    for i,j in (map(int,l) for l in map(str.split,fi)):
        print((PODZOL_TEMPLATE if (i,j) in herb_locations else PATH_TEMPLATE).format(j=i-di,i=j-dj),file=fo)
