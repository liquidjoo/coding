def dfs(v):
    if dfs_check[v]:
        return

    dfs_check[v] = True
    for i in range(adj[v].__len__()):
        x = adj[v][i]
        dfs(x)

def bfs(v):
    queue_list = list()
    queue_list.append(v)
    bfs_check[v] = True

    while queue_list.__len__() != 0:
        x = queue_list.pop()

        for i in range(adj[v].__len__()):
            x = adj[v][i]

            if not bfs_check[x]:
                queue_list.append(x)
                bfs_check[x] = True


m, n, v = input().split()

m = int(m)
n = int(n)
v = int(v)

adj = [list() for _ in range(m+1)]
dfs_check = [False for _ in range(m+1)]
bfs_check = [False for _ in range(m+1)]

for _ in range(n):
    x, y = input().split()
    x = int(x)
    y = int(y)
    # 인접리스트 생성
    adj[x].append(y)
    adj[y].append(x)

