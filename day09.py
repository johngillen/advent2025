import util.aoc as aoc

part1 = 0
part2 = 0

area = lambda a, b: (abs(a[0] - b[0]) + 1) * (abs(a[1] - b[1]) + 1)

tiles = []
rectangles = {}

for line in aoc.lines():
    newtile = tuple(aoc.ints(line))
    for tile in tiles:
        if (newtile, tile) not in rectangles:
            rectangles[(tile, newtile)] = area(tile, newtile)
    tiles.append(newtile)

rectangle = 0
for a in tiles:
    for b in tiles:
        if area(a, b) > rectangle:
            for a2, b2 in zip(tiles, tiles[1:]):
                if not any([(a2[0] <= min(a[0], b[0]) and b2[0] <= min(a[0], b[0])),
                            (a2[1] <= min(a[1], b[1]) and b2[1] <= min(a[1], b[1])),
                            (a2[0] >= max(a[0], b[0]) and b2[0] >= max(a[0], b[0])),
                            (a2[1] >= max(a[1], b[1]) and b2[1] >= max(a[1], b[1]))]):
                    break
            else: rectangle = area(a, b)

part1 = max(rectangles.values())
part2 = rectangle

print(f'part 1: {part1}')
# aoc.post(2025, 9, 1, part1)
print(f'part 2: {part2}')
# aoc.post(2025, 9, 2, part2)
