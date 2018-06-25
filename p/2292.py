number = int(input())

if number == 1:
    print(1)
    exit()
index = 0
while True:
    if 1+(6*index) < number:
        index += 1
    else:
        print(index+1)
        break
