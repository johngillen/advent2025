import util.aoc as aoc

part1 = 0
part2 = 0

def invalid(id):
    sid, pow10 = str(id), len(str(id))
    return sid[:pow10 // 2] * 2 == sid

def invalid2(id):
    sid, pow10 = str(id), len(str(id))
    for i in range(1, pow10 // 2 + 1):
        if sid[:i] * (pow10 // i) == sid: return True
    return False

for line in aoc.lines():
    for idranges in line.split(','):
        a, b = aoc.uints(idranges)
        for i in range(a, b + 1):
            if invalid(i): part1 += i
            if invalid2(i): part2 += i

print(f'part 1: {part1}')
# aoc.post(2025, 2, 1, part1)
print(f'part 2: {part2}')
# aoc.post(2025, 2, 2, part2)
