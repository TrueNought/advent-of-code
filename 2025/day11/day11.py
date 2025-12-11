with open('day11_input.txt') as input:
    input = input.read().splitlines()
    graph = {}
    for line in input:
        node, *neighbors = line.split()
        graph[node[:-1]] = neighbors


def part_one(input):
    dp = {}

    def dfs(u):
        if u in dp:
            return dp[u]

        if u == 'out':
            return 1
        
        paths = 0
        for v in graph[u]:
            paths += dfs(v)
        
        dp[u] = paths
        return paths
    
    return dfs('you')


def part_two(input):
    dp = {}
    
    def dfs(u, dest):
        key = (u, dest)
        if key in dp:
            return dp[key]

        if u == dest:
            return 1

        paths = 0
        for v in graph.get(u, []):
            paths += dfs(v, dest)

        dp[key] = paths
        return paths

    dac_fft = dfs('dac', 'fft')
    
    if dac_fft != 0:
        return dfs('svr', 'dac') * dac_fft * dfs('fft', 'out')
    
    return dfs('svr', 'fft') * dfs('fft', 'dac') * dfs('dac', 'out')


print('part1', part_one(input))
print('part2', part_two(input))