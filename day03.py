import util.aoc as aoc

part1 = 0
part2 = 0

def joltage(bank, batteries):
    jolts = 0
    def pull_battery():
        nonlocal bank
        battery = max(bank) if batteries == 1 else max(bank[:-batteries + 1])
        bank = bank[bank.index(battery) + 1:]
        return battery, bank
    while batteries:
        battery, bank = pull_battery()
        jolts = jolts * 10 + battery
        batteries -= 1
    return jolts

for line in aoc.lines():
    bank = aoc.digits(line)
    part1 += joltage(bank, 2)
    part2 += joltage(bank, 12)

print(f'part 1: {part1}')
# aoc.post(2025, 3, 1, part1)
print(f'part 2: {part2}')
# aoc.post(2025, 3, 2, part2)
