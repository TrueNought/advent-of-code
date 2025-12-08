from functools import lru_cache

with open('day07_input.txt') as input:
    input = input.read().splitlines()

def part_one(input):
    beams = [0] * len(input[0])
    start = None
    result = 0

    for row in input:
        if not start:
            start = row.find('S')
            beams[start] = 1
            continue
        
        for j, col in enumerate(row):
            if col == '^' and beams[j] == 1:
                beams[j] = 0
                beams[j - 1] = 1
                beams[j + 1] = 1
                result += 1
    
    return result
        

def part_two(input):
    start = input[0].find('S')
    
    @lru_cache(maxsize=None)
    def backtrack(i, j):
        if i == len(input) - 1:
            return 1
        
        if input[i + 1][j] == '^':
            return backtrack(i + 1, j - 1) + backtrack(i + 1, j + 1)
        else:
            return backtrack(i + 1, j)

    return backtrack(1, start)


print('part1', part_one(input))
print('part2', part_two(input))