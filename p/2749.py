
f = [0, 1]

def fib(n):
    for i in range(2, int(n)+1):
        f.append(int(f[i-1]) + int(f[i-2]))

    return f[n]


number = input()
print(fib(int(number)) % 1000000)