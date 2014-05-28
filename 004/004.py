from itertools import dropwhile, ifilter, product, starmap


print max(ifilter(lambda s: str(s) == str(s)[::-1], starmap(lambda x, y: x * y, product(range(999, 99, -1), repeat=2))))
