import util.aoc as aoc
from collections import defaultdict

part1 = 0
part2 = 0

lines = aoc.lines()
start = (0, lines[0].index('S'))

queue = {start}
splitters = {()}
graph = defaultdict(set)
exits = set()

left = lambda x, y: (x + 2, y - 1)
right = lambda x, y: (x + 2, y + 1)
down = lambda x, y: (x + 2, y)

while queue:
    x, y = queue.pop()
    try:
        if lines[x + 2][y] == '^':
            if left(x, y) not in splitters:
                splitters.add(left(x, y))
            graph[left(x, y)].add((x, y))
            graph[right(x, y)].add((x, y))
            queue.add(left(x, y))
            queue.add(right(x, y))
        else:
            graph[down(x, y)].add((x, y))
            queue.add(down(x, y))
    except IndexError:
        exits.add((x, y))

memo = {start: 1}

def timelines(node):
    if node in memo:
        return memo[node]
    else:
        memo[node] = sum(timelines(parent) for parent in graph[node])
        return memo[node]

part1 = len(splitters) - 1
part2 = sum(timelines(exit) for exit in exits)

print(f'part 1: {part1}')
# aoc.post(2025, 7, 1, part1)
print(f'part 2: {part2}')
# aoc.post(2025, 7, 2, part2)
