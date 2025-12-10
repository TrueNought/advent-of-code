with open('day09_input.txt') as input:
    input = [tuple(map(int, line.split(','))) for line in input]


def part_one(input):
    best = 0

    for a in range(len(input)):
        y1, x1 = input[a]
        for b in range(a, len(input)):
            y2, x2 = input[b]
            best = max(best, (abs(y1 - y2) + 1) * (abs(x1 - x2) + 1))
    
    return best


def part_two(input):
    areas = []
    edges = []

    for a in range(len(input)):
        y1, x1 = input[a]
        for b in range(a + 1, len(input)):
            y2, x2 = input[b]
            area = (abs(y1 - y2) + 1) * (abs(x1 - x2) + 1)
            areas.append((area, (x1, y1), (x2, y2)))

            if x1 == x2 or y1 == y2:
                edges.append(((x1, y1), (x2, y2)))

    areas.sort(reverse=True)

    for area, (x1, y1), (x2, y2) in areas:
        valid = True

        left, right = sorted([x1, x2])
        top, bottom = sorted([y1, y2])

        for (a1, b1), (a2, b2) in edges:
            e_left, e_right = sorted([a1, a2])
            e_top, e_bottom = sorted([b1, b2])
            # must be at least one edge outside rectangle (hence bounding it)
            outside = right <= e_left or left >= e_right or bottom <= e_top or top >= e_bottom

            if not outside:
                valid = False
                break
        
        if valid:
            return area


print('part1', part_one(input))
print('part2', part_two(input))