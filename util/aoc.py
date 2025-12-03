import re

ints = lambda s: list(map(int, re.findall(r"-?\d+", s)))
uints = lambda s: list(map(int, re.findall(r"\d+", s)))
digits = lambda s: list(map(int, re.findall(r"\d", s)))

def lines(dir = 'input'):
    from datetime import datetime, timezone, timedelta
    year, day = datetime.now(timezone(timedelta(hours=-5))).year, \
                datetime.now(timezone(timedelta(hours=-5))).day
    
    f = open(f'{dir}/day{day:0>2}.txt')
    return [line.rstrip() for line in f.readlines()]

def post(year, day, part, answer):
    import requests
    cookie = open('util/cookie.txt', 'r').readline().strip()
    contact = open('util/contact.txt', 'r').readline().strip()
    url = f'https://adventofcode.com/{year}/day/{day}/answer'
    data = {'level': part, 'answer': answer}
    response = requests.post(url, cookies={'session': cookie}, headers={'User-Agent': contact}, data=data)
    match response.text:
        case text if 'That\'s the right answer!' in text:
            print('+1 star')
        case text if 'too high' in text:
            print('too high')
        case text if 'too low' in text:
            print('too low')
        case text if 'That\'s not the right answer' in text:
            print('wrong answer')
        case text if 'You gave an answer too recently' in text:
            print('too soon')
        case _:
            print('unknown response')
