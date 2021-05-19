import factorial

MENU_TEXT = '''Permutation and Combination Calculator
by MathBot.

Format:
Permutasi >> nPk

Example:
3P2
>> 6

-help to see this again
-exit to go back to main menu'''

EXC_TEXT = '''Invalid input!
try again or -exit to go back to main menu'''

def sum_permutation(n, k):
    return (factorial.calc_factorial(n)) // (factorial.calc_factorial(n - k))

def sum_combination(n, k):
    return (factorial.calc_factorial(n)) // ((factorial.calc_factorial(n - k)) * factorial.calc_factorial(k))

def main(text):
    try:
        if text == '-help':
            return(MENU_TEXT)
        elif 'p' in text:
            text = text.replace(' ', '')
            n, k = text.split('p')
            n = int(n)
            k = int(k)
            return sum_permutation(n, k)
        elif 'c' in text:
            text = text.replace(' ', '')
            n, k = text.split('c')
            n = int(n)
            k = int(k)
            return sum_combination(n, k)
        else:
            return EXC_TEXT
    except:
        return EXC_TEXT



DEBUG = False

if DEBUG:
    while True:
        print(main(input()))