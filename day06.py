import util.aoc as aoc

part1 = 0
part2 = 0

problems = [[]]
problems270 = [[]]
operations = []

f = open('input/day06.txt')
lines = f.read().splitlines()

for line in lines[:-1]:
    ints = [[num] for num in aoc.uints(line)]
    problems = [a + b for a, b in zip(problems + [[]] * len(ints), ints)]

for line in list(zip(*lines[:-1]))[::-1]:
    ints = aoc.uints(''.join(line))
    if ints: problems270[-1] += ints
    else: problems270 += [[]]

operations = lines[-1].split()

for nums, op in zip(problems, operations):
    part1 += eval(op.join(map(str, nums)))

for nums, op in zip(problems270, operations[::-1]):
    part2 += eval(op.join(map(str, nums)))

print(f'part 1: {part1}')
# aoc.post(2025, 6, 1, part1)
print(f'part 2: {part2}')
# aoc.post(2025, 6, 2, part2)
