n, m = input().split()

n = int(n)
m = int(m) - 1

result = list()
circle_queue = [i for i in range(1, n+1)]


while circle_queue.__len__() != 0:
    if circle_queue.__len__() <= m:
        m = m%int(circle_queue.__len__())

    point = circle_queue.pop(m)
    left_list = circle_queue[m:]
    right_list = circle_queue[:m]
    circle_queue = left_list + right_list

    result.append(point)


print(result)