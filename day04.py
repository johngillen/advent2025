import util.aoc as aoc

part1 = 0
part2 = 0

grid = aoc.grid()

def forklift(grid):
    for x, row in enumerate(grid):
        for y, val in enumerate(row):
            if val != '@': continue
            neighbors = 0
            for nx, ny in [(x + dx, y + dy) for dx, dy in aoc.COMPASS8]:
                if aoc.valid((nx, ny), grid) and grid[nx][ny] == '@':
                    neighbors += 1
            if neighbors < 4: yield (x, y)

part1 = len(list(forklift(grid)))

while True:
    changed = False
    for x, y in forklift(grid):
        grid[x][y] = 'x'
        changed = True
        part2 += 1
    if not changed: break

print(f'part 1: {part1}')
# aoc.post(2025, 4, 1, part1)
print(f'part 2: {part2}')
# aoc.post(2025, 4, 2, part2)
