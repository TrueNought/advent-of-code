with open('day05_input.txt') as input:
    input = input.read().strip()

def merge_intervals(intervals):
    intervals.sort()
    merged = [intervals[0]]

    for i in range(1, len(intervals)):
        curr = intervals[i]
        prev = merged[-1]

        if curr[0] <= prev[1]:
            merged[-1][1] = max(curr[1], prev[1])
        else:
            merged.append(curr)
    
    return merged


def part_one(input):
    intervals, ingredients = input.split('\n\n')
    ingredients = ingredients.splitlines()
    intervals = [list(map(int, r.split('-'))) for r in intervals.splitlines()]

    intervals = merge_intervals(intervals)
    result = 0

    for ingredient in ingredients:
        for start, end in intervals:
            if start <= int(ingredient) <= end:
                result += 1
    
    return result


def part_two(input):
    intervals, _ = input.split('\n\n')
    intervals = [list(map(int, r.split('-'))) for r in intervals.splitlines()]
    intervals = merge_intervals(intervals)

    result = 0
    for start, end in intervals:
        result += (end - start + 1)
    
    return result


print('part1', part_one(input))
print('part2', part_two(input))