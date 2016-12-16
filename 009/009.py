import math


print reduce(lambda a, bc: a * bc[0][0] * int(bc[0][1]), filter(lambda z: len(z[1]) > 0, map(lambda x: (x[0], filter(lambda y: x[0] + y[0] + y[1] == 1000, map(lambda b: (b, math.sqrt(x[0]**2 + b**2)), x[1]))), map(lambda x: (x, range(x, 500)), range(1, 499))))[0])
