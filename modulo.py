MENU_TEXT = '''Modulo Calculator
by MathBot.

Example:
5 mod 3
>> 2

2.5 % 1
>> 0.5

-exit to go back to main menu'''

EXC_TEXT = '''Invalid input!
try again or -exit to go back to main menu'''


def modulo(text):
    try:
        text = text.replace(' ', '')
        a, b = text.split('mod')

        return float(a) % float(b)
    except:
        return EXC_TEXT


DEBUG = False

if DEBUG:
    while True:
        x = input()
        print(modulo(x))