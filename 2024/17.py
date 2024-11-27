import networkx as nx

def load_file(part):
    with open(f"everybody_codes_e2024_q17_p{part}.txt") as f:
        lines = f.read().splitlines()
    return {(i,j) for i,line in enumerate(lines) for j,c in enumerate(line) if c=="*"}

def mh(p1,p2):
    x1,y1 = p1
    x2,y2 = p2
    return abs(x1-x2)+abs(y1-y2)

def constellation_size(graph):
    tree = nx.minimum_spanning_tree(graph)
    return sum(mh(p1,p2) for p1,p2 in tree.edges()) + len(graph.nodes())

for part in (1,2,3):
    points = load_file(part)
    G = nx.Graph()
    for point1 in points:
        for point2 in points:
            if point1 < point2 and (part < 3 or mh(point1,point2) < 6): # avoid duplicates
                G.add_edge(point1,point2,weight=mh(point1,point2))

    if part < 3:
        print(constellation_size(G))
    else:
        sizes = [constellation_size(G.subgraph(c)) for c in nx.connected_components(G)]
        sizes.sort()
        a,b,c = sizes[-3:]
        print(a*b*c)


import PIL.Image as Image
with open(f"everybody_codes_e2024_q17_p{part}.txt") as f:
    lines = f.read().splitlines()
img = Image.new("1",(len(lines[0]),len(lines)))
for point in points:
    img.putpixel(point[::-1],1)
img = img.resize((img.width,img.height*2),Image.Resampling.NEAREST)
img.save("17-bw.png")

img = Image.new("HSV",(len(lines[0]),len(lines)))
for i,c in enumerate(nx.connected_components(G)):
    hue = (i*111-65)%256
    size = constellation_size(G.subgraph(c))
    for point in c:
        img.putpixel(point[::-1],(hue,255,50+(size*205//sizes[-1])))
img.convert("RGB").resize((img.width*3,img.height*5),Image.Resampling.NEAREST).save("17-coloured3.png")
