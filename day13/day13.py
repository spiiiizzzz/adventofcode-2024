# alright this is not gonna be easy
import re
import math
import sys

# Why have a custom round defined? Cause floating point arithmetic is stupid
def custom_round(n: float) -> int:
    n_str = str(n).split('.')
    if len(n_str) == 1:
        return int(n)
    else:
        if n_str[1][:2] == '00' or (n_str[1][0] == '0') if len(n_str[1]) == 1 else False:
            return int(n_str[0])
        elif n_str[1][:2] == '99' or (n_str[1][0] == '9') if len(n_str[1]) == 1 else False:
            return int(n_str[0]) + 1
    raise ValueError(f"not close enough to an integer {n_str}")

### Here is the system of equations i used to calculate this:
# a, b -> how many times do you press a and b
#
# x1a + x2b = X
# y1a + y2b = Y
# 
# x1a = X - x2b
# a = (X - x2b)/x1
# 
# y1((X - x2b)/x1) + y2b = Y
# (y1X - y1x2b)/x1 + y2b = Y
# y1X/x1 - y1x2b/x1 + y2b = Y
# y2b - y1x2b/x1 = Y - y1X/x1
# b(y2 - y1x2/x1) = Y - y1X/x1
# b = (Y - y1X/x1) / (y2 - y1x2/x1)
# 
# No, I'm not gonna try to simplify this, i'm too lazy for that
def button_combination(button_a: tuple[int], button_b: tuple[int], val: tuple[int]) -> tuple[int] | None:
    try:
        b = custom_round((val[1]*button_a[0] - (button_a[1]*val[0])) / (button_b[1]*button_a[0] - (button_a[1]*button_b[0])))
        a = custom_round((val[0] - button_b[0]*b)/button_a[0])
    except:
        return None

    # i hate floating point arithemtic
    if a < 0 or b < 0 or a >= 100 or b >= 100:
        return None
    else:
        return (a, b)

def main():
    with open("/home/saas/Projects/aoc-2024/day13/input.txt", "r") as f:
        inp = f.read().split('\n\n')

        machines = []
        for i in inp:
            a, b, p = i.split('\n')[:3]
            machines.append((
                (int(re.search('X\\+[0-9]*', a).group(0).split('+')[1]), int(re.search('Y\\+[0-9]*', a).group(0).split('+')[1])),
                (int(re.search('X\\+[0-9]*', b).group(0).split('+')[1]), int(re.search('Y\\+[0-9]*', b).group(0).split('+')[1])),
                (int(re.search('X\\=[0-9]*', p).group(0).split('=')[1]), int(re.search('Y\\=[0-9]*', p).group(0).split('=')[1]))
            ))

        total = 0
        for m in machines:
            res = button_combination(m[0], m[1], m[2])
            if res != None:
                total += res[0]*3 + res[1]

        print(total)



if __name__ == "__main__":
    main()