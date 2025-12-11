import util.aoc as aoc
from functools import lru_cache

part1 = 0
part2 = 0

g = {}

for line in aoc.lines():
    node = line.split(': ')[0]
    neighbors = line.split(': ')[1].split(' ')
    g[node] = set(neighbors)

def paths(start, end):
    @lru_cache(None)
    def helper(node):
        if node == end: return 1
        return sum(helper(neighbor) for neighbor in g[node])
    return helper(start)    

def badpaths(start, end):
    @lru_cache(None)
    def helper(node, mask = 0):
        if node == end: return mask == 3
        return sum(helper(neighbor, mask | ({'fft': 1, 'dac': 2}.get(node, 0))) for neighbor in g[node])
    return helper(start)

part1 = paths('you', 'out')
part2 = badpaths('svr', 'out')

print(f'part 1: {part1}')
# aoc.post(2025, 11, 1, part1)
print(f'part 2: {part2}')
# aoc.post(2025, 11, 2, part2)
