import util.aoc as aoc

part1 = 0
part2 = 0

dial = 50

for line in aoc.lines():
    rot, val = line[0], int(line[1:])
    dial += val if rot == 'R' else -val
    part2 += abs(dial // 100)
    dial %= 100
    part1 += dial == 0

print(f'part 1: {part1}')
# aoc.post (2025, 1, 1, part1)
print(f'part 2: {part2}')
# aoc.post(2025, 1, 2, part2)
