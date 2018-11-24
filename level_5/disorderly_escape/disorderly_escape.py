"""
    Used Burnside Lemma and Polya Enumeration over the course of a week.

    'G' is a group of permutations on 'X', which is our set of rows or columns of the
    grid we're given. For example, if w=2 and h=3 and we're looking at rows,

    X = {
        [a, b],
        [c, d],
        [e, f]
    }

    Again, 'G' consists of all permutations on 'X', which means G contains all
    combinations of moving around the elements in 'X', including keeping them
    in place.

    We can show that 'X' has 6 row permutations and 2 column permutations, denoted by
    S_3 (for the set of three rows) and S_2 (for the set of two columns).
"""

from math import floor
from collections import Counter

def gcd(x, y):
    while y > 0:
        x, y = y, x % y
    return x

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def number_of_cycles(cyclic_permutations):
    """
        CONSULTED: https://math.stackexchange.com/questions/1536031/counting-cycle-structures-in-s-n

        Given a set_size 'S' and a list of the permutations on the set, if we count
        the number of occurrences of each cycle length, we can compute the denominator of
        our calculation by this formula:

        (number of cycle occurrences)! * (length of cycle)^(number of cycle occurrences)

        When iterating over Counter's items, item(1) is number of cycles and item(0) is length of cycle
    """
    set_size = sum(cyclic_permutations)

    permutation_count = Counter(cyclic_permutations)
    product = 1
    for item in permutation_count.items():
        # number, length = item
        try:
            product *= factorial(item[1]) * pow(item[0], item[1])
        except TypeError:
            print item

    return factorial(set_size) / product 
    

def partitions(remaining, last_step):
    """
        Originally used a regular recursive function and returned a list of lists
        to be used in the main answer() function. To speed up, I looked up Python 
        generators of lists and implemented this. I used my "the_grandest_staircase_of_them_all"
        code to help write this function, since they perform almost similar integer partitioning.
    """
    
    yield [remaining]
    limit = int(floor(remaining / 2.0))
    for num in range(last_step, limit + 1): 

        results = [
            [num] + partition
            for partition in partitions(remaining - num, num)
        ]

        for result in results:
            yield result
            
def answer(w, h, s):
    """
        Iterate through the products of the cycle indices of the width and height permutations.
        For loop will iterate w * h number of times

        Least common multiple not in math module, have to use GCD.


    """
    cycle_sum = 0

    for w_perm in partitions(w, 1):
        for h_perm in partitions(h, 1):

            count = number_of_cycles(w_perm) * number_of_cycles(h_perm)

            """
                Each cycle product contributes a certain amount, which can be
                expressed as the gcd() of the two cycles. Another way of representing
                the cycle contribution is (cycle_one * cycle_two) / (lcm(cycle_one, cycle_two)).
            """
            contribution = 0

            for w_cycle in w_perm:
                for h_cycle in h_perm:
                    contribution += gcd(w_cycle, h_cycle)

            cycle_sum += count * pow(s, contribution)
    

    """
        At the end, we divide by the total number of combinations, which is
        just w! * h!. They were excluded until the end to make hand calculations, and 
        subsequently the code, easier to traverse.
    """

    return cycle_sum / (factorial(w) * factorial(h))

print answer(2, 3, 4)

for item in partitions(2, 1):
    print item

print(number_of_cycles([4, 4]))
