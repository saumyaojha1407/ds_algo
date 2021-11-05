def dfs(graph, start, visited):
    visited.add(start)
    # print(start)
    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited


graph = {'0': set(['1', '2']),
         '1': set(['0', '3', '4']),
         '2': set(['0']),
         '3': set(['1']),
         '4': set(['2', '3']),
         '5':set(['4'])}
visited = set()
for edge in graph:
    visited = dfs(graph, edge, visited)
print(visited)