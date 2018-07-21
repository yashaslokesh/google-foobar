import math



from functools import lru_cache

@lru_cache(maxsize = None)
def calculate(remaining_bricks, last_step):
    options = 0
    if remaining_bricks/(last_step + 1) <= 2:
        print(f"{remaining_bricks} : {last_step}")
        return 1
    else:
        options += 1
    for i in range(last_step + 1, math.ceil(remaining_bricks/2)):
        # return 1 + calculate(remaining_bricks - i, i)
        options += calculate(remaining_bricks - i, i)
    return options

def answer(n):
    return calculate(n, 0) - 1

number = int(input("Enter number of bricks: "))
staircase_options = answer(number)
print(staircase_options)