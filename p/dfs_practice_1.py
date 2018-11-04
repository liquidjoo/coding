def dfs(v):
    if dfs_check[v]:
        return

    dfs_check[v] = True
    for i in range(adj[v].__len__()):
        x = adj[v][i]
        dfs(x)


m, n, v = input().split()

m = int(m)
n = int(n)
v = int(v)

adj = [list() for _ in range(m+1)]
dfs_check = [False for _ in range(m+1)]

for _ in range(n):
    x, y = input().split()
    x = int(x)
    y = int(y)
    adj[x].append(y)
