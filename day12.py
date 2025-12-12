import util.aoc as aoc

part1 = 0
part2 = 0

lines = aoc.lines()
size = [0] * 6

for i in range(6):
    for x, line in enumerate(lines[(i * 5) + 1:(i + 1) * 5]):
        size[i] += line.count('#')

for line in lines[30:]:
    x, y = aoc.uints(line)[0], aoc.uints(line)[1]
    counts = aoc.uints(line)[2:]
    if (x * y) - sum(counts[i] * size[i] for i in range(6)) > 0: 
        part1 += 1

part2 = 'push the button!' if part1 else 0

print(f'part 1: {part1}')
# aoc.post(2025, 12, 1, part1)
print(f'part 2: {part2}')
# aoc.post(2025, 12, 2, part2)
