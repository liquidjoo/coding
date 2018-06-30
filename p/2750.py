count_num = int(input())

num_list = list()
for i in range(count_num):
    num = int(input())
    num_list.append(num)

# num_list.sort(reverse=True)
# print(num_list)

for j in range(1, count_num):
    tmp = j - 1
    pivot_value = num_list[j]

    while num_list[tmp] > pivot_value and tmp >= 0:
        num_list[tmp+1] = num_list[tmp]
        tmp -= 1
    num_list[tmp+1] = pivot_value

for k in range(0, count_num):
    print(num_list[k])

# bigO = n + (n-1)*(n-m)+ n  ( n > m)