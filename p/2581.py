start_num = int(input())
end_num = int(input())

result = list()
sum = 0
for i in range(start_num, end_num+1):
    count = 0
    for j in range(1, i+1):
        if count >= 3:
            break
        if i % j == 0:
            count += 1

    if count == 2:
        sum+=i
        result.append(i)

if sum == 0:
    print(-1)
else:
    print(sum)
    print(result[0])

