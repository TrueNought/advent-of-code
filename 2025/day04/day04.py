from collections import deque

with open('day04_input.txt') as input:
    input = input.read().splitlines()

def part_one(input):
    rows = len(input)
    cols = len(input[0])
    degrees = [[0] * cols for _ in range(rows)]
    result = 0

    for i in range(rows):
        for j in range(cols):
            if input[i][j] == '@':
                for di, dj in [(0, 1), (1, -1), (1, 0), (1, 1)]:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < rows and 0 <= nj < cols and input[ni][nj] == '@':
                        degrees[i][j] += 1
                        degrees[ni][nj] += 1

                if degrees[i][j] < 4:
                    result += 1

    return result


def part_two(input):
    input = [list(line) for line in input]
                
    rows = len(input)
    cols = len(input[0])
    degrees = [[0] * cols for _ in range(rows)]
    result = 0
    q = deque([])

    for i in range(rows):
        for j in range(cols):
            if input[i][j] == '@':
                for di, dj in [(0, 1), (1, -1), (1, 0), (1, 1)]:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < rows and 0 <= nj < cols and input[ni][nj] == '@':
                        degrees[i][j] += 1
                        degrees[ni][nj] += 1
                if degrees[i][j] < 4:
                    q.append((i, j))

    visited = set(q)
    while q:
        i, j = q.popleft()
        result += 1
        input[i][j] = '.'

        for di, dj in [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, -1), (1, 0), (1, 1)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < rows and 0 <= nj < cols and input[ni][nj] == '@':
                degrees[ni][nj] -= 1

                if degrees[ni][nj] < 4 and (ni, nj) not in visited:
                    visited.add((ni, nj))
                    q.append((ni, nj))

    return result


print('part1', part_one(input))
print('part2', part_two(input))