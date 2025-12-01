with open('day01_input.txt') as input:
    input = input.read().splitlines()

def part_one(input):
    result = 0
    curr = 50

    for line in input:
        direction = line[0]
        amount = int(line[1:])

        if direction == 'L':
            curr -= amount
        elif direction == 'R':
            curr += amount

        curr = curr % 100
        if curr == 0:
            result += 1
    
    return result


def part_two(input):
    result = 0
    curr = 50

    for line in input:
        direction = line[0]
        amount = int(line[1:])
        prev = curr

        if direction == 'L':
            curr -= amount
            result += abs(curr // 100)
            
            # prev zero, curr not multiple of 100 -> ensure no overcount
            if prev == 0 and curr % 100 != 0:
                result -= 1
            # prev nonzero, curr multiple of 100 -> ensure no undercount
            elif prev != 0 and curr % 100 == 0:
                result += 1

        elif direction == 'R':
            curr += amount
            result += curr // 100

        curr = curr % 100
    
    return result

print('part1', part_one(input))
print('part2', part_two(input))