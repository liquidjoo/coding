def dfs(v):
    if check[v]:
        return
    check[v] = True

    for k in range(0, int(adj[v].__len__())):
        dfs(adj[v][k])


def bfs(v):
    queue_list = list()
    queue_list.append(v)
    check2[v] = True

    while int(queue_list.__len__()) == 0:
        x = queue_list.pop()
        print(x)

        for k in range(0, int(adj[x].__len__())):
            y = adj[x][k]
            if not check2[y]:
                queue_list.append(y)
                check2[y] = True




n, m, v = input().split()

n = int(n)
m = int(m)
v = int(v)

adj = [list() for _ in range(0, n+1)]
check = [False for _ in range(0, n+1)]
check2 = [False for _ in range(0, n+1)]

for i in range(0, m):
    x, y = input().split()
    x = int(x)
    y = int(y)

    adj[x].append(y)
    adj[y].append(x)

dfs(v)