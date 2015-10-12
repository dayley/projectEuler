__author__ = 'LD'

'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000
'''


def threefives(origin, limit):
    numlist = []
    while origin <= limit:
        numlist.append(origin)
        origin += 1
    else:
        return numlist


def sieve(numlist):
    final = []
    for n in numlist:
        if n % 3 is 0:
            final.append(n)
        elif n % 5 is 0:
            final.append(n)
    return final

def adder(final):
    return sum(final)

print(adder(sieve(threefives(1, 1000))))
