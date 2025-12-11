from functools import lru_cache

with open('day10_input.txt') as input:
    input = input.read().splitlines()


def part_one(input):
    result = 0

    for line in input:
        _, *tuples, _ = line.split()
        _ = [True if x == '#' else False for x in _.strip('[]')]
        buttons = []
        for t in tuples:
            inner = t.strip('()')
            buttons.append([int(x) for x in inner.split(',')])

        def backtrack(i, state):
            if i == len(buttons):
                if state == _:
                    return 0
                return float('inf')

            best = backtrack(i + 1, state)
            for pos in buttons[i]:
                state[pos] = not state[pos]
            
            best = min(best, 1 + backtrack(i + 1, state))
            for pos in buttons[i]:
                state[pos] = not state[pos]

            return best
        
        result += backtrack(0, [False] * len(_))
    
    return result



def part_two(input):
    result = 0

    for line in input:
        _, *tuples, joltages = line.split()
        joltages = [int(x) for x in joltages.strip('{}').split(',')]
        buttons = []
        for t in tuples:
            inner = t.strip('()')
            buttons.append([int(x) for x in inner.split(',')])

        @lru_cache(maxsize=None)
        def backtrack(i, remaining):
            if i == len(buttons):
                if all(v == 0 for v in remaining):
                    return 0
                return float('inf')
            
            remaining_lst = list(remaining)
            allowed_presses = min(remaining[j] for j in buttons[i])

            # skip pressing
            best = backtrack(i + 1, remaining)

            # press up to allowed num of presses
            for n in range(1, allowed_presses + 1):
                for pos in buttons[i]:
                    remaining_lst[pos] -= 1
                best = min(best, backtrack(i + 1, tuple(remaining_lst)) + n)

            return best
        
        result += backtrack(0, tuple(joltages))

    return result

print('part1', part_one(input))
print('part2', part_two(input))