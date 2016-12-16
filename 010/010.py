from itertools import takewhile


def generate_primes():
    """
    Taken from http://code.activestate.com/recipes/117119-sieve-of-eratosthenes/
    """

    D = {}  
    q = 2  
    while True:
        if q not in D:
            yield q        
            D[q * q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        q += 1


print sum(takewhile(lambda x: x < 2000000, generate_primes()))
