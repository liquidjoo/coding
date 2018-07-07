def dfs(v):
    print(adj)
    if check[v]:
        return
    check[v] = True
    print(v)
    for i in range(0, int(adj[v].__len__())):
        x = adj[v][i]
        dfs(x)


def bfs(v):
    queue_list = list()
    queue_list.append(v)
    check2[v] = True

    while queue_list.__len__() != 0:
        x = queue_list.pop(0)
        print(x)
        # queue_list = queue_list[1:]
        print(queue_list)

        for i in range(0, int(adj[x].__len__())):
            print(adj)
            y = adj[x][i]
            if not check2[y]:
                queue_list.append(y)
                check2[y] = True


n, m, v = input().split()

n = int(n)
m = int(m)
v = int(v)

adj = [list() for _ in range(n+1)]
check = [False for _ in range(n+1)]
check2 = [False for _ in range(n+1)]

{}
for i in range(1, m+1):
    x, y = input().split()
    x = int(x)
    y = int(y)
    adj[x].append(y)
    adj[y].append(x)

bfs(v=v)
# dfs(v=v)
