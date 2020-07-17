from math import sqrt
from pprint import pprint as pp
# import pprint

def isPrime(x):
    if x<2:
        return False
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

results = {x: x**2 for x in range(1, 101) if isPrime(x)}

# pp.pprint(results)
pp(results)
