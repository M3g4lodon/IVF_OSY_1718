import re

UNREAD = [r'#.+\n', r'[ \t\n]+']

INT = [r'\d+']

VAR = [r'[a-zA-Z]\w+']

A_EXP = INT + VAR

A_EXP_A = [r'\+', r'-', r'x']

B_VAR = [r'true', r'false']

B_OP = [r'(\w+):not']

B_OP_A = [r'(\w+):=', r'(\w+):<=']

B_EXP = B_OP + B_OP_A

B_EXP_B = [r'and', r'or']

COM = [r'(\w+):skip',
       r'(\w+):[a-zA-Z]\w+:=\d+|[a-zA-Z]\w+',
       r'']


def clear_program(input):
    res = input
    for pat in UNREAD:
        res = re.sub(pat, '', res)
    return res


if __name__ == '__main__':
    ex0 = """# TD1 : Exercise 3

while 1:not(X=Y) do{
    if 2:X>Y
    then {3:X:=X-Y} # Bluelue
    else {4:Y:=Y-X}
}"""
    prog=clear_program(ex0)
