data = input()
for i in range(int(data.__len__())):
    if (i+1) % 10 == 0:
        print(data[i])
    else:
        print(data[i], end='')
