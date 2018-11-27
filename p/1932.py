n = int(input())

d = [[0 for _ in range(n)] for _ in range(n)]
a = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    a[i] = input().split()

d[0][0] = int(a[0][0])
for i in range(n):
    if i == 0:
        continue
    for j in range(len(a[i])):
        # print(i, j)
        # if j==0 or i==j:
        #     d[i][j] = int(d[i-1][j]) + int(a[i][j])
        # else:
        #     d[i][j] = max(int(d[i-1][j-1]), int(d[i-1][j])) + int(a[i][j])
        d[i][j] = max(int(d[i - 1][j - 1]), int(d[i - 1][j])) + int(a[i][j])

# print(d)
print(max(d[n-1]))
