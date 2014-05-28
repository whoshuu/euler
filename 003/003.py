def prime_factors(n):
    d = 2
    while n > 1:
        while n % d == 0:
            yield d
            n /= d
        d = d + 1
        if d**2 > n:
            if n > 1:
                yield n
            break


print max(prime_factors(600851475143))
