
raw_data = list(input())

stack_data = list()

for x in raw_data:
    stack_data.append(x)
    top = len(stack_data) - 1
    tmp = top - 1

    if stack_data[top] not in ('(', ')', '[', ']') and stack_data[top - 1] not in ('(', ')', '[', ']'):
        q = stack_data.pop(top)
        w = stack_data.pop(top - 1)
        stack_data.append(q+w)

        top = len(stack_data) - 1
        tmp = top - 1

    for _ in range(top):
        if stack_data[tmp] not in ('(', ')', '[', ']'):
            tmp -= 1

    if tmp == top - 1:
        if stack_data[tmp] == '(' and stack_data[top] == ')':
            stack_data.pop(top)
            stack_data.pop(tmp)
            stack_data.append(2)

            top = len(stack_data) - 1
            tmp = top - 1

            if top > 0:
                if stack_data[top] not in ('(', ')', '[', ']') and stack_data[top - 1] not in ('(', ')', '[', ']'):
                    q = stack_data.pop(top)
                    w = stack_data.pop(top - 1)
                    stack_data.append(int(q) + int(w))

        elif stack_data[tmp] == '[' and stack_data[top] == ']':
            stack_data.pop(top)
            stack_data.pop(tmp)
            stack_data.append(3)

            top = len(stack_data) - 1
            tmp = top - 1

            if top > 0:
                if stack_data[top] not in ('(', ')', '[', ']') and stack_data[top - 1] not in ('(', ')', '[', ']'):
                    q = stack_data.pop(top)
                    w = stack_data.pop(top - 1)
                    stack_data.append(int(q) + int(w))

        else:
            continue
        # print(stack_data)

    else:
        if stack_data[tmp] == '(' and stack_data[top] == ')':
            stack_data.pop(top)
            stack_data.pop(tmp)
            b = stack_data.pop(tmp)
            stack_data.append(int(b)*2)

            top = len(stack_data) - 1
            tmp = top - 1

            if top > 0:
                if stack_data[top] not in ('(', ')', '[', ']') and stack_data[top - 1] not in ('(', ')', '[', ']'):
                    q = stack_data.pop(top)
                    w = stack_data.pop(top - 1)
                    stack_data.append(int(q) + int(w))

        elif stack_data[tmp] == '[' and stack_data[top] == ']':
            stack_data.pop(top)
            stack_data.pop(tmp)
            b = stack_data.pop(tmp)
            stack_data.append(int(b) * 3)

            top = len(stack_data) - 1
            tmp = top - 1

            if top > 0:
                if stack_data[top] not in ('(', ')', '[', ']') and stack_data[top - 1] not in ('(', ')', '[', ']'):
                    q = stack_data.pop(top)
                    w = stack_data.pop(top - 1)
                    stack_data.append(int(q) + int(w))

        else:
            continue


if len(stack_data) == 1:
    print(stack_data.pop())

else:
    print(0)


