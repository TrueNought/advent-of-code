import math

with open('day02_input.txt') as input:
    input = input.read().strip().split(',')

def part_one(input):
    result = 0

    for interval in input:
        start, end = interval.split('-')
        min_l = math.ceil(len(start) / 2)
        max_l = len(end) // 2
        
        start, end = int(start), int(end)

        for k in range(min_l, max_l + 1):
            for n in range(10 ** (k - 1), 10 ** k):
                n_seq = n * (10 ** k + 1)
                if n_seq > end:
                    break
                if start <= n_seq <= end:
                    result += n_seq
    
    return result


def part_two(input):
    result = 0

    for interval in input:
        start, end = interval.split('-')
        max_l = len(end) // 2
        n_start, n_end = int(start), int(end)

        invalid = set()
        for k in range(1, max_l + 1):
            for n in range(10 ** (k - 1), 10 ** k):
                for times in range(2, (len(end) // k) + 1):
                    n_seq = int(str(n) * times)

                    if n_start <= n_seq <= n_end and n_seq not in invalid:
                        invalid.add(n_seq)
                        result += n_seq
    
    return result

print('part1', part_one(input))
print('part2', part_two(input))