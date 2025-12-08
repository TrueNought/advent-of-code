import math

with open('day08_input.txt') as input:
    input = [tuple(map(int, line.split(','))) for line in input]
    n = len(input)
    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            cost = math.dist(input[i], input[j])
            edges.append((cost, i, j))
    
    edges.sort()


def part_one(input):
    parent = list(range(n))
    size = [1] * n

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(x, y):
        rx, ry = find(x), find(y)
        if rx != ry:
            if (size[rx] < size[ry]):
                parent[rx] = ry
                size[ry] += size[rx]
            else:
                parent[ry] = rx
                size[rx] += size[ry]
    
    steps = 0
    for _, x, y in edges:
        if steps >= 1000:
            break
        union(x, y)
        steps += 1
    
    size.sort(reverse=True)
    return size[0] * size[1] * size[2]
    

def part_two(input):
    parent = list(range(n))
    size = [1] * n
    prev = None

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(x, y):
        nonlocal prev
        rx, ry = find(x), find(y)
        if rx != ry:
            if (size[rx] < size[ry]):
                parent[rx] = ry
                size[ry] += size[rx]
            else:
                parent[ry] = rx
                size[rx] += size[ry]
            
            prev = (x, y)
    
    for _, x, y in edges:
        union(x, y)
    
    a, b = prev
    return input[a][0] * input[b][0]


print('part1', part_one(input))
print('part2', part_two(input))