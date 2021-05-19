import factorial

MENU_TEXT = '''Combination Calculator
by MathBot.

Format:
Kombinasi >> nCk

Example:
3C2
>> 3


-help to see this again
-exit to go back to main menu'''

EXC_TEXT = '''Invalid input!
try again or -exit to go back to main menu'''

def sum_combination(n, k):
    return (factorial.calc_factorial(n)) // ((factorial.calc_factorial(n - k)) * factorial.calc_factorial(k))

def main(text):
    try:
        if text == '-help':
            return(MENU_TEXT)
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