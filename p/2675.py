input_count = input()
for i in range(int(input_count)):
    recursive_number, data = input().split()
    for j in range(int(str(data).__len__())):
        print(data[j] * int(recursive_number), end="")