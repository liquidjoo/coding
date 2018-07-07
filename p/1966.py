test_case = int(input())

for _ in range(test_case):
    n, m = input().split()
    n = int(n)
    m = int(m)
    priority_list = input().split()

    priority_queue = list()
    find_value = int(priority_list[m])

    while priority_list.__len__() != 0:
        index = priority_list.index(max(priority_list))
        max_value = priority_list.pop(index)
        priority_queue.append(int(max_value))

    index = 1
    for i in priority_queue:
        if i == find_value:
            print(index)
            break
        else:
            index += 1

