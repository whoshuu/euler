print sum([a * b for a, b in zip(map(lambda n: sum(filter(lambda x: not x % n, range(1000))), (3, 5, 15)), (1, 1, -1))])
