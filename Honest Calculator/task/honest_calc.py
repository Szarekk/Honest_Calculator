def is_num(input_string):
    try:
        float(input_string)
        return True
    except ValueError:
        return False


def calculate_result(x, oper, y):
    if oper == '+':
        return x + y
    if oper == '-':
        return x - y
    if oper == '*':
        return x * y
    if oper == '/' and y != 0:
        return x / y
    else:
        return msg_3


def use_memory(x, y, memory):
    if x == 'M':
        x = memory
    elif y == 'M':
        y = memory
    return x, y


def yes_or_no(msg):
    answer = ''
    while answer not in ['y', 'n']:
        print(msg)
        answer = input()
    return True if answer == 'y' else False


def is_one_digit(v):
    return True if v > -10 and v < 10 and v.is_integer() else False


def check(v1, v2, v3):
    msg = ''
    if is_one_digit(v1) and is_one_digit(v2):
        msg += msg_6
    if v1 == 1 or v2 == 1:
        msg += msg_7
    if (v1 == 0 or v2 == 0) and (v3 == '*' or v3 == '-'):
        msg += msg_8
    if msg != '':
        print(msg)
        msg = msg_9 + msg
        print(msg)


memory = 0.0
msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"

while True:
    print(msg_0)
    calc = input()
    x, oper, y = calc.split()
    x, y = use_memory(x, y, memory)
    if not (is_num(x) and is_num(y)):
        print(msg_1)
    elif oper not in '+-*/':
        print(msg_2)
    else:
        x, y = float(x), float(y)
        check(x, y, oper)
        result = calculate_result(x, oper, y)
        print(result)
        if result != msg_3:
            if yes_or_no(msg_4):
                memory = result
            if not yes_or_no(msg_5):
                break
