import util.aoc as aoc

part1 = 0
part2 = 0

ranges = []
ids = []

inrange = lambda lo, hi, n: lo <= n <= hi

for line in aoc.lines():
    ints = aoc.uints(line)
    if len(ints) == 2: ranges.append((ints[0], ints[1]))
    if len(ints) == 1: ids.append(ints[0])

while True:
    merged = True
    for _ in range(len(ranges)):
        lo, hi = ranges.pop(0)
        for _ in range(len(ranges)):
            lo2, hi2 = ranges.pop(0)
            if inrange(lo, hi, lo2) or inrange(lo, hi, hi2):
                ranges.append((min(lo, lo2), max(hi, hi2)))
                merged = False
                break
            else: ranges.append((lo2, hi2))
        else: ranges.append((lo, hi))
    if merged: break

part1 = sum(any(inrange(lo, hi, id) for lo, hi in ranges) for id in ids)
part2 = sum(hi - lo + 1 for lo, hi in ranges)

print(f'part 1: {part1}')
# aoc.post(2025, 5, 1, part1)
print(f'part 2: {part2}')
# aoc.post(2025, 5, 2, part2)
