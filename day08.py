import util.aoc as aoc
import networkx as nx

part1 = 0
part2 = 0

dist = lambda a, b: ((a[0]-b[0])**2 + (a[1]-b[1])**2 + (a[2]-b[2])**2 )**0.5

dists = {}
G = nx.Graph()

for line in aoc.lines():
    new = tuple(aoc.ints(line))
    for node in G.nodes: dists[(new, node)] = dist(new, node)
    G.add_node(new)
shortest = sorted(dists, key=dists.get)

for a, b in shortest[:1000]:
    G.add_edge(a, b)
top3 = sorted(list(nx.connected_components(G)), key=len, reverse=True)[:3]

while len(list(nx.connected_components(G))) > 1:
    a, b = shortest.pop(0)
    G.add_edge(a, b)

part1 = len(top3[0]) * len(top3[1]) * len(top3[2])
part2 = a[0] * b[0]

print(f'part 1: {part1}')
# aoc.post(2025, 8, 1, part1)
print(f'part 2: {part2}')
# aoc.post(2025, 8, 2, part2)
