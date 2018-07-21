
def answer(M, F):
    mach, facula = long(M), long(F)
    generations = 0
    while mach != 1 and facula != 1:
        if mach % facula == 0 or facula % mach == 0:
            return "impossible"
        elif mach > facula:
            factor = mach/facula
            mach = mach - facula*factor
            generations += factor
        else:
            factor = facula/mach
            facula = facula - mach*factor
            generations += factor
    return generations + max(mach, facula) - 1



print(answer(4,7))
    
print("\n")

answer1 = answer(2, 1)
print(answer1 == 1)
print("answer1: {0}".format(answer1))

answer2 = answer(4, 7)
print(answer2 == 4)

answer3 = answer(2, 4)
print(answer3 == "impossible")

print("\n")
