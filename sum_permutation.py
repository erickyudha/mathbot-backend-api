import factorial

MENU_TEXT = '''Permutation Calculator
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
        else:
            return EXC_TEXT
    except:
        return EXC_TEXT