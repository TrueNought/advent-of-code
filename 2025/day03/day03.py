with open('day03_input.txt') as input:
    input = input.read().splitlines()

def part_one(input):
    result = 0
    for line in input:
        best_first = line[0]
        best_second = '0'

        for i in range(1, len(line)):
            curr = line[i]
            if curr > best_first and i + 1 != len(line):
                best_first = curr
                best_second = '0'
            elif curr > best_second:
                best_second = curr

        result += int(best_first + best_second)
    
    return result


def part_two(input):
    result = 0
    for line in input:
        drop = len(line) - 12
        stack = []

        for n in line:
            while drop > 0 and stack and stack[-1] < n:
                stack.pop()
                drop -= 1
            stack.append(n)
        result += int(''.join(stack[:12]))

    return result
            

print('part1', part_one(input))
print('part2', part_two(input))