with open('day06_input.txt') as input:
    input = [line.strip('\n') for line in input]

def part_one(input):
    input = [line.split() for line in input]
    result = 0
    for c in range(len(input[0])):
        op = input[-1][c]
        total = 0 if op == '+' else 1
        for r in range(len(input) - 1):
            if op == '+':
                total += int(input[r][c])
            else:
                total *= int(input[r][c])

        result += total
    
    return result
            

def part_two(input):
    result = 0
    total = 0

    for c in range(len(input[0])):
        # if we're in a blank column
        if c + 1 < len(input[0]) and input[-1][c + 1] != ' ':
            result += total
            continue
        # if new operation encountered
        if input[-1][c] != ' ':
            op = input[-1][c]
            total = 0 if op == '+' else 1
        
        curr = ''
        for r in range(len(input) - 1):
            if input[r][c] != ' ':
                curr += input[r][c]
        
        if op == '+':
            total += int(curr)
        else:
            total *= int(curr)

    result += total
    return result


print('part1', part_one(input))
print('part2', part_two(input))