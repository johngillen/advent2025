import util.aoc as aoc
import re
import z3

part1 = 0
part2 = 0

machines = []

for line in aoc.lines():
    lights = [1 if c == '#' else 0 for c in re.search(r'\[(.*)\]', line).groups()[0]]
    buttons = [set(aoc.uints(match[0])) for match in re.finditer(r'(\([\d,]+\))', line)]
    joltages = aoc.uints(re.search(r'{(.*?)}', line).groups()[0])
    machines.append((lights, buttons, joltages))

for lights, buttons, _ in machines:
    s = z3.Solver()
    btn_vars = [z3.Int(f'btn_{i}') for i in range(len(buttons))]
    solution_len = float('inf')
    for var, button in zip(btn_vars, buttons):
        s.add(0 <= var, var <= len(lights))
    for i in range(len(lights)):
        connected = [var for var, button in zip(btn_vars, buttons) if i in button]
        s.add(lights[i] == z3.Sum(connected) % 2)
    while s.check() == z3.sat:
        m = s.model()
        solution_len = sum(m[var].as_long() for var in btn_vars)
        s.add(z3.Sum([var for var in btn_vars]) < solution_len)
    part1 += solution_len

for _, buttons, joltage in machines:
    s = z3.Solver()
    btn_vars = [z3.Int(f'btn_{i}') for i in range(len(buttons))]
    solution_len = float('inf')
    for var, button in zip(btn_vars, buttons):
        s.add(0 <= var, var <= max(joltage[i] for i in button))
    for i in range(len(joltage)):
        s.add(z3.Sum([var for var, button in zip(btn_vars, buttons) if i in button]) == joltage[i])
    while s.check() == z3.sat:
        m = s.model()
        solution_len = sum(m[var].as_long() for var in btn_vars)
        s.add(z3.Sum([var for var in btn_vars]) < solution_len)
    part2 += solution_len

print(f'part 1: {part1}')
# aoc.post(2025, 10, 1, part1)
print(f'part 2: {part2}')
# aoc.post(2025, 10, 2, part2)
