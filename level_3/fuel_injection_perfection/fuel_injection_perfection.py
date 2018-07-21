
def answer(n):
    num = long(n)
    min_operations = 0
    while num > 1:
        if not num & 1:
            num /= 2
        else:
            num += 1 if (num % 4 == 3 and not num == 3) else -1
        min_operations += 1
    return min_operations 

print(answer(4))
print(answer(15))

