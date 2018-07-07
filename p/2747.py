fibo_list = [0, 1]

n = int(input())

if n == 0:
    print(0)

elif n == 1:
    print(1)

elif 0 <= n <= 45:
    for i in range(2, n + 1):
        k = fibo_list[i - 1] + fibo_list[i - 2]
        fibo_list.append(k)

    print(fibo_list[i])
