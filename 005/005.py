from collections import Counter
from itertools import starmap


def prime_factors(n):
    factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            factors.append(d)
            n /= d
        d = d + 1
        if d**2 > n:
            if n > 1:
                factors.append(n)
            break
    return factors


print reduce(lambda x, y: x * y, (starmap(pow, list(reduce(lambda a, b: Counter({e: max(a[e], b[e]) for e in set(list(a)+list(b))}), map(lambda l: Counter(l), map(prime_factors, range(2, 21)))).items()))))
