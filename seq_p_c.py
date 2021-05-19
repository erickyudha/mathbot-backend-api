from itertools import permutations, combinations

MENU_TEXT = '''Permutation and Combination Sequance Calculator
by MathBot

Format:


Example:
3P2
>> 6

3C2
>> 3

-help to see this again
-exit to go back to main menu'''

EXC_TEXT = '''Invalid input!
try again or -exit to go back to main menu'''

def perm_seq(perm_list):
    perm = permutations(perm_list)
    result = ''
    for i in list(perm):
        result = result + f'{i}\n'
    return result

def comb_seq(comb_list, r):
    comb = combinations(comb_list, r)
    result = ''
    for i in list(comb):
        result = result + f'{i}\n'
    return result

def main(text):


DEBUG = False

if DEBUG:
    while True:
        box = []
        for i in range(3):
            box.append(input())
        print(perm_seq(box))
        print(comb_seq(box))