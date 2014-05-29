from collections import Counter
from itertools import combinations, dropwhile, permutations, takewhile
import json
import math


def is_prime(n):
    if n % 2 == 0 and n > 2: 
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))


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


def get_primes(count):
    frequency_list = json.loads(count[0])
    s = ''
    primes = []
    for l in frequency_list:
        for _ in range(l[1]):
            s += l[0]
    for p in set([''.join(x) for x in permutations(s, 4)]):
        if is_prime(int(p)):
            primes.append(p)
    return list(set(primes))


def get_differences(l):
    differences = []
    for i in combinations(l, 2):
        differences.append(abs(int(i[0]) - int(i[1])))
    counter = Counter(differences)
    differences = []
    for k, v in counter.iteritems():
        if v >= 2 and k * 2 in counter.keys():
            differences.append(k)
    l = [int(i) for i in l]
    for i in l:
        for d in differences:
            if i + d in l and i + 2*d in l and len(filter(lambda x: x < 1000, l)) == 0:
                return [i, i + d, i + 2*d]


print filter(lambda x: x != None, map(get_differences, map(get_primes, filter(lambda x: x[1] >= 3, Counter(map(lambda x: json.dumps(Counter(str(x)).most_common()), takewhile(lambda x: x < 10000, dropwhile(lambda x: x < 1000, generate_primes())))).most_common()))))
