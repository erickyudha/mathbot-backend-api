MENU_TEXT = '''Factorial Calculator
by MathBot.

-exit to go back to main menu'''

EXC_TEXT = '''Invalid input!
try again or -exit to go back to main menu'''

def calc_factorial(num):
    num = int(num)
    if num == 0:
        return 1
    else:
        return num * calc_factorial(num - 1)

def factorial(text):
    try:
        int(text)
        if int(text) < 0 or not text.isnumeric():
            return EXC_TEXT
        else:
            return f'{text}! = {calc_factorial(text)}'
    except:
        return EXC_TEXT

DEBUG = False

if DEBUG:
    while True:
        x = input()
        print(factorial(x))
