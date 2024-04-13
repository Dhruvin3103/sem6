from collections import deque

def ford_fulkerson(G, source, sink):
    max_flw = 0
    allpath,path_flws = [],[]
    while True:
        paths = bfs(G, source, sink)
        if not paths:
            break
        for path in paths:
            path_flw = min(G[path[i]][path[i+1]] for i in range(len(path)-1))
            allpath.append(path)
            path_flws.append(path_flw)
            max_flw += path_flw
            G = modify_G(G, path, path_flw)
    return max_flw, allpath, path_flws
def bfs(G, source, sink):
    paths = []
    queue = deque([(source, [source])])
    while queue:
        u, path = queue.popleft()
        for v, capacity in enumerate(G[u]):
            if capacity > 0 and v not in path:
                if v == sink:
                    paths.append(path + [v])
                else:
                    queue.append((v, path + [v]))
    return paths
def modify_G(G, path, flw):
    for i in range(len(path)-1):
        u, v = path[i], path[i+1]
        G[u][v] -= flw
        G[v][u] += flw  
    return G

#        D   M   K   B  P  s
G =     [[0, 8, 14, 0, 0, 0],
         [0, 0, 14, 12, 0, 0],
         [0, 6, 0, 0, 10, 0],
         [0, 0, 10, 0, 0, 17],
         [0, 0, 0, 7, 0, 6],
         [0, 0, 0, 0, 0, 0]]
source = 0
sink = 5
max_flw, allpath, path_flws = ford_fulkerson(G, source, sink)
print(f"Maximum flow: {max_flw}")
print("<-----All augmenting paths and their corresponding flows----->")
for i, path in enumerate(allpath):
    print(f"Path --> {path}, flow along path: {path_flws[i]}")