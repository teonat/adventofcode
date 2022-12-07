import csv
import re

stacks = """
[S]                 [T] [Q]        
[L]             [B] [M] [P]     [T]
[F]     [S]     [Z] [N] [S]     [R]
[Z] [R] [N]     [R] [D] [F]     [V]
[D] [Z] [H] [J] [W] [G] [W]     [G]
[B] [M] [C] [F] [H] [Z] [N] [R] [L]
[R] [B] [L] [C] [G] [J] [L] [Z] [C]
[H] [T] [Z] [S] [P] [V] [G] [M] [M]
 1   2   3   4   5   6   7   8   9 
"""

moves = """move 6 from 1 to 7
move 2 from 2 to 4
move 2 from 7 to 4
move 6 from 4 to 3
move 1 from 5 to 1
move 3 from 8 to 3
move 15 from 3 to 4
move 6 from 5 to 9
move 14 from 4 to 2
move 3 from 2 to 7
move 1 from 2 to 7
move 9 from 9 to 1
move 3 from 2 to 1
move 7 from 6 to 7
move 1 from 6 to 8
move 2 from 9 to 1
move 9 from 2 to 3
move 8 from 3 to 9
move 1 from 1 to 4
move 1 from 8 to 6
move 1 from 6 to 2
move 5 from 9 to 8
move 2 from 9 to 1
move 1 from 4 to 2
move 17 from 1 to 9
move 1 from 3 to 1
move 3 from 2 to 3
move 2 from 4 to 5
move 12 from 7 to 3
move 16 from 9 to 2
move 5 from 7 to 5
move 2 from 1 to 2
move 1 from 3 to 6
move 1 from 4 to 6
move 1 from 7 to 3
move 1 from 6 to 3
move 7 from 3 to 4
move 5 from 8 to 3
move 1 from 6 to 7
move 7 from 3 to 4
move 6 from 3 to 1
move 2 from 4 to 8
move 1 from 5 to 2
move 10 from 4 to 5
move 3 from 5 to 2
move 2 from 8 to 9
move 5 from 2 to 8
move 1 from 3 to 5
move 2 from 5 to 8
move 12 from 5 to 7
move 1 from 4 to 2
move 5 from 9 to 4
move 1 from 2 to 5
move 6 from 1 to 3
move 6 from 3 to 5
move 10 from 7 to 4
move 2 from 7 to 3
move 4 from 7 to 6
move 1 from 9 to 5
move 12 from 2 to 1
move 1 from 8 to 7
move 3 from 7 to 4
move 4 from 4 to 8
move 7 from 5 to 3
move 1 from 2 to 4
move 10 from 1 to 5
move 2 from 1 to 2
move 4 from 6 to 7
move 8 from 8 to 3
move 5 from 4 to 9
move 12 from 3 to 8
move 4 from 3 to 8
move 2 from 9 to 2
move 3 from 5 to 4
move 1 from 3 to 5
move 1 from 7 to 6
move 14 from 4 to 6
move 6 from 5 to 9
move 8 from 2 to 8
move 3 from 5 to 7
move 21 from 8 to 4
move 16 from 4 to 9
move 8 from 6 to 2
move 4 from 6 to 1
move 1 from 4 to 6
move 2 from 4 to 8
move 3 from 1 to 8
move 2 from 4 to 6
move 1 from 6 to 2
move 3 from 8 to 4
move 2 from 2 to 5
move 2 from 5 to 7
move 1 from 8 to 9
move 1 from 4 to 9
move 1 from 1 to 6
move 3 from 6 to 3
move 3 from 2 to 3
move 1 from 4 to 6
move 3 from 6 to 7
move 10 from 9 to 7
move 1 from 4 to 7
move 6 from 8 to 3
move 1 from 6 to 8
move 2 from 2 to 5
move 1 from 2 to 1
move 1 from 8 to 9
move 1 from 2 to 8
move 1 from 1 to 9
move 7 from 9 to 1
move 1 from 8 to 5
move 7 from 1 to 7
move 3 from 5 to 8
move 3 from 7 to 2
move 1 from 8 to 4
move 1 from 2 to 4
move 2 from 4 to 6
move 5 from 3 to 1
move 9 from 7 to 2
move 6 from 3 to 8
move 8 from 2 to 7
move 2 from 6 to 4
move 2 from 1 to 7
move 2 from 1 to 4
move 24 from 7 to 4
move 4 from 8 to 9
move 2 from 7 to 5
move 1 from 5 to 2
move 1 from 3 to 8
move 4 from 2 to 8
move 13 from 9 to 2
move 2 from 8 to 6
move 3 from 9 to 6
move 26 from 4 to 2
move 1 from 5 to 7
move 2 from 6 to 2
move 2 from 4 to 1
move 7 from 2 to 1
move 15 from 2 to 6
move 8 from 2 to 8
move 4 from 6 to 8
move 9 from 2 to 9
move 13 from 6 to 7
move 6 from 1 to 9
move 2 from 2 to 4
move 4 from 1 to 6
move 3 from 8 to 3
move 1 from 4 to 9
move 2 from 6 to 7
move 1 from 4 to 3
move 3 from 3 to 2
move 14 from 7 to 4
move 5 from 9 to 5
move 9 from 8 to 5
move 7 from 9 to 6
move 2 from 5 to 6
move 2 from 9 to 2
move 10 from 5 to 1
move 1 from 3 to 1
move 2 from 8 to 1
move 1 from 9 to 2
move 1 from 7 to 5
move 4 from 2 to 1
move 1 from 9 to 8
move 3 from 4 to 1
move 1 from 8 to 6
move 12 from 1 to 5
move 1 from 1 to 6
move 1 from 7 to 5
move 4 from 6 to 9
move 2 from 2 to 4
move 1 from 9 to 6
move 1 from 1 to 5
move 2 from 9 to 7
move 10 from 6 to 5
move 1 from 6 to 7
move 20 from 5 to 1
move 1 from 7 to 9
move 2 from 9 to 1
move 3 from 5 to 1
move 2 from 8 to 4
move 2 from 8 to 7
move 1 from 5 to 9
move 1 from 8 to 4
move 22 from 1 to 7
move 5 from 4 to 8
move 1 from 5 to 9
move 19 from 7 to 4
move 2 from 9 to 1
move 1 from 5 to 9
move 10 from 1 to 8
move 1 from 9 to 1
move 1 from 8 to 3
move 8 from 4 to 7
move 1 from 5 to 6
move 3 from 4 to 5
move 1 from 5 to 9
move 11 from 7 to 4
move 4 from 4 to 9
move 1 from 6 to 2
move 1 from 3 to 9
move 5 from 9 to 4
move 5 from 7 to 9
move 23 from 4 to 2
move 17 from 2 to 7
move 2 from 2 to 8
move 4 from 4 to 7
move 1 from 4 to 5
move 2 from 5 to 2
move 5 from 8 to 9
move 5 from 2 to 7
move 9 from 7 to 5
move 11 from 9 to 2
move 1 from 4 to 3
move 5 from 8 to 7
move 3 from 8 to 5
move 2 from 1 to 3
move 2 from 3 to 9
move 1 from 5 to 8
move 5 from 7 to 5
move 15 from 5 to 4
move 2 from 8 to 1
move 2 from 5 to 1
move 4 from 4 to 1
move 1 from 8 to 7
move 8 from 2 to 1
move 4 from 2 to 8
move 2 from 7 to 4
move 5 from 8 to 6
move 5 from 7 to 9
move 4 from 6 to 5
move 7 from 4 to 8
move 1 from 6 to 1
move 1 from 3 to 1
move 2 from 5 to 1
move 7 from 1 to 5
move 5 from 1 to 3
move 4 from 7 to 9
move 4 from 3 to 9
move 2 from 9 to 7
move 6 from 9 to 2
move 1 from 4 to 1
move 1 from 3 to 5
move 1 from 2 to 5
move 5 from 9 to 4
move 4 from 4 to 6
move 1 from 8 to 9
move 8 from 4 to 3
move 7 from 7 to 3
move 5 from 1 to 3
move 11 from 5 to 9
move 1 from 7 to 6
move 2 from 3 to 5
move 1 from 3 to 1
move 3 from 6 to 2
move 2 from 5 to 1
move 2 from 1 to 2
move 3 from 1 to 5
move 5 from 9 to 2
move 2 from 6 to 8
move 2 from 3 to 8
move 4 from 9 to 7
move 3 from 5 to 2
move 2 from 1 to 8
move 1 from 9 to 8
move 1 from 9 to 2
move 4 from 7 to 9
move 11 from 8 to 7
move 1 from 8 to 2
move 6 from 9 to 7
move 3 from 7 to 1
move 13 from 2 to 7
move 24 from 7 to 1
move 2 from 2 to 6
move 1 from 8 to 3
move 1 from 9 to 3
move 5 from 2 to 4
move 1 from 2 to 5
move 1 from 6 to 2
move 1 from 6 to 3
move 1 from 2 to 4
move 3 from 7 to 3
move 2 from 1 to 7
move 2 from 3 to 8
move 2 from 7 to 8
move 9 from 3 to 2
move 3 from 4 to 8
move 1 from 5 to 1
move 9 from 2 to 1
move 3 from 4 to 9
move 1 from 7 to 8
move 6 from 3 to 9
move 2 from 1 to 5
move 15 from 1 to 3
move 13 from 3 to 9
move 11 from 1 to 4
move 5 from 4 to 1
move 6 from 3 to 6
move 4 from 4 to 8
move 6 from 1 to 4
move 1 from 5 to 2
move 1 from 2 to 1
move 3 from 4 to 2
move 2 from 8 to 5
move 2 from 4 to 2
move 9 from 9 to 3
move 9 from 3 to 5
move 2 from 9 to 4
move 5 from 2 to 6
move 1 from 1 to 8
move 1 from 4 to 1
move 10 from 9 to 2
move 9 from 2 to 4
move 10 from 4 to 1
move 3 from 1 to 3
move 4 from 1 to 2
move 5 from 2 to 4
move 2 from 5 to 2
move 4 from 1 to 7
move 10 from 5 to 4
move 2 from 2 to 4
move 1 from 9 to 2
move 2 from 3 to 5
move 1 from 3 to 5
move 3 from 6 to 7
move 8 from 4 to 9
move 6 from 6 to 1
move 4 from 9 to 5
move 2 from 9 to 1
move 1 from 2 to 6
move 6 from 5 to 2
move 3 from 7 to 9
move 4 from 8 to 2
move 1 from 7 to 9
move 1 from 5 to 3
move 2 from 7 to 4
move 1 from 7 to 1
move 14 from 1 to 9
move 1 from 1 to 9
move 1 from 3 to 8
move 3 from 2 to 5
move 2 from 4 to 2
move 6 from 8 to 1
move 1 from 2 to 1
move 5 from 1 to 9
move 1 from 1 to 7
move 2 from 8 to 5
move 1 from 5 to 4
move 1 from 6 to 1
move 8 from 2 to 7
move 2 from 6 to 1
move 9 from 9 to 5
move 11 from 4 to 8
move 4 from 7 to 4
move 6 from 4 to 6
move 1 from 7 to 4
move 6 from 6 to 7
move 1 from 5 to 9
move 6 from 8 to 9
move 8 from 9 to 5
move 1 from 4 to 5
move 15 from 9 to 3
move 3 from 1 to 4
move 6 from 7 to 2
move 3 from 4 to 9
move 2 from 7 to 3
move 1 from 7 to 3
move 1 from 7 to 2
move 2 from 8 to 1
move 3 from 8 to 5
move 2 from 1 to 7
move 8 from 3 to 6
move 3 from 6 to 5
move 1 from 6 to 1
move 10 from 5 to 7
move 6 from 5 to 4
move 4 from 2 to 4
move 6 from 5 to 1
move 6 from 1 to 8
move 2 from 9 to 2
move 2 from 9 to 7
move 6 from 3 to 7
move 1 from 3 to 5
move 1 from 1 to 9
move 2 from 8 to 1
move 2 from 5 to 4
move 3 from 3 to 7
move 10 from 4 to 6
move 1 from 9 to 7
move 12 from 7 to 3
move 12 from 3 to 8
move 2 from 1 to 5
move 1 from 1 to 3
move 13 from 8 to 1
move 7 from 7 to 1
move 13 from 6 to 9
move 1 from 7 to 4
move 6 from 5 to 3
move 3 from 4 to 3
move 6 from 3 to 1
move 10 from 9 to 4
move 2 from 7 to 6
move 8 from 1 to 9
move 3 from 2 to 9
move 1 from 3 to 5
move 1 from 3 to 5
move 1 from 1 to 4
move 6 from 9 to 3
move 2 from 6 to 7
move 4 from 9 to 5
move 4 from 1 to 6
move 1 from 2 to 4
move 6 from 1 to 4
move 3 from 9 to 3
move 3 from 6 to 8
move 3 from 8 to 7
move 5 from 5 to 1
move 1 from 3 to 9
move 1 from 9 to 5
move 1 from 3 to 2
move 2 from 5 to 1
move 1 from 6 to 9
move 1 from 6 to 3
move 2 from 9 to 7
move 2 from 8 to 1
move 1 from 3 to 2
move 1 from 2 to 5
move 1 from 7 to 1
move 7 from 7 to 9
move 12 from 1 to 9
move 1 from 5 to 2
move 1 from 7 to 1
move 13 from 4 to 7
move 1 from 9 to 4
move 5 from 7 to 3
move 4 from 9 to 1
move 8 from 7 to 9
move 3 from 2 to 3
move 4 from 3 to 7
move 5 from 4 to 6
move 3 from 9 to 4
move 10 from 1 to 5
move 3 from 4 to 7
move 16 from 9 to 2
move 3 from 9 to 2
move 6 from 5 to 3
move 4 from 6 to 2
move 1 from 4 to 6
move 2 from 6 to 8
move 1 from 5 to 2
move 1 from 5 to 8
move 7 from 7 to 2
move 16 from 2 to 1
move 1 from 5 to 1
move 10 from 2 to 8
move 14 from 8 to 5
move 2 from 2 to 6
move 1 from 2 to 5
move 2 from 2 to 1
move 8 from 1 to 7
move 4 from 1 to 7
move 2 from 1 to 7
move 5 from 3 to 2
move 1 from 1 to 6
move 2 from 2 to 5
move 4 from 1 to 7
move 1 from 2 to 8
move 1 from 2 to 8
move 3 from 6 to 7
move 10 from 7 to 5
move 1 from 2 to 8
move 27 from 5 to 9
move 1 from 5 to 6
move 1 from 6 to 4
move 1 from 4 to 3
move 3 from 3 to 7
move 4 from 3 to 6
move 2 from 6 to 4
move 3 from 8 to 1
move 2 from 6 to 1
move 12 from 7 to 8
move 2 from 3 to 9
move 1 from 9 to 2
move 1 from 2 to 8
move 2 from 1 to 2
move 6 from 3 to 8
move 1 from 7 to 4
move 15 from 9 to 5
move 7 from 9 to 4
move 1 from 2 to 1
move 16 from 8 to 2
move 8 from 5 to 2
move 24 from 2 to 9
move 3 from 1 to 2
move 24 from 9 to 1
move 5 from 5 to 9
move 3 from 4 to 1
move 1 from 7 to 6
move 1 from 6 to 3
move 1 from 3 to 2
move 3 from 2 to 3
move 1 from 5 to 6
move 1 from 2 to 7"""

csv_str = ''
for i, row in enumerate(stacks.removesuffix('\n').removeprefix('\n').split('\n')[::-1]):
    if i == 0: 
        csv_str += row.removeprefix(' ').removesuffix(' ').replace('   ', ',') + '\n'
    else:
        csv_str += row.replace('    ', ',').replace(' ', ',') + '\n'

a = csv.DictReader(csv_str.split(), delimiter=',')
csv_dict = dict(enumerate(a))
stack_dict = {}
for i, data in csv_dict.items():
    for k, v in data.items():
        if k not in stack_dict:
            stack_dict[k] = v.replace('[','').replace(']','')
        else:
            stack_dict[k] += v.replace('[','').replace(']','')

for move in moves.split('\n'):
    amount, frm, to = re.findall(r'move (\d+) from (\d+) to (\d+)', move)[0]
    for crt in stack_dict[frm][-int(amount):][::-1]:  # Revert because they're add last first (LIFO)
        print(crt)
        stack_dict[to] += crt
    stack_dict[frm] = stack_dict[frm][:-int(amount)]

solution = ''    
for k, v in stack_dict.items():
    solution += v[-1:] 
print(solution)


# Part two

a = csv.DictReader(csv_str.split(), delimiter=',')
csv_dict = dict(enumerate(a))
stack_dict = {}
for i, data in csv_dict.items():
    for k, v in data.items():
        if k not in stack_dict:
            stack_dict[k] = v.replace('[','').replace(']','')
        else:
            stack_dict[k] += v.replace('[','').replace(']','')

for move in moves.split('\n'):
    amount, frm, to = re.findall(r'move (\d+) from (\d+) to (\d+)', move)[0]
    stack_dict[to] += stack_dict[frm][-int(amount):]
    stack_dict[frm] = stack_dict[frm][:-int(amount)]

solution = ''    
for k, v in stack_dict.items():
    solution += v[-1:] 
print(solution)