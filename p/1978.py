n = int(input())
n_list = input().split()

result = 0
for i in range(0, n):
    count = 0
    for j in range(1, int(n_list[i])+1):

        if int(n_list[i]) % j == 0:
            count += 1

    if count == 2:
        result += 1

print(result)


