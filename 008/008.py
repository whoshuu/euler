import os


with open(os.path.join(os.path.dirname(__file__), 'number.txt'), 'r') as f:
    number = f.readline().strip('\n')


consecutive = 13
largest = 0
largest_start = 0

for start in range(len(number) - consecutive + 1):
    p = reduce(lambda x, y: int(x) * int(y), number[start:start + consecutive])
    if p > largest:
        largest_start = start
        largest = p
print number[largest_start:largest_start + consecutive], largest
