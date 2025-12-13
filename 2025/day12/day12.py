with open('day12_input.txt') as input:
    input = input.read().splitlines()


def part_one(input):
    sizes = []
    for i in range(1, 27, 5):
        count = 0
        for line in input[i:i+3]:
            count += line.count('#')
        sizes.append(count)

    result = 0

    for line in input[30:]:
        area, shape_counts = line.split(':')
        area = area.split('x')
        area = int(area[0]) * int(area[1])
        shape_counts = [int(x) for x in shape_counts.strip().split()]
        
        curr = 0
        for size, count in zip(sizes, shape_counts):
            curr += size * count
        
        if curr <= area:
            result += 1
    
    return result


print('part1', part_one(input))
