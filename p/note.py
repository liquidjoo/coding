# 합병 정렬


def merge_sort(list):
    if len(list) <= 1:
        return list

    mid = len(list) // 2
    left_list = list[:mid]
    right_list = list[mid:]

    left_list = merge_sort(left_list)
    right_list = merge_sort(right_list)
    return merge(left_list, right_list)


def merge(left_list, right_list):
    result = list()

    while len(left_list) > 0 or len(right_list) > 0:

        if len(left_list) > 0 and len(right_list) > 0:
            if left_list[0] > right_list[0]:
                result.append(right_list[0])
                right_list = right_list[1:]

            else:
                result.append(left_list[0])
                left_list = left_list[1:]

        elif len(left_list) > 0:
            result.append(left_list[0])
            left_list = left_list[1:]

        elif len(right_list) > 0:
            result.append(right_list[0])
            right_list = right_list[1:]

    return result


def radix_sort(ordered_list):

    is_loop = False
    postion = 1

    while not is_loop:
        is_loop = True
        queue_list = [list() for _ in range(10)]

        for num in ordered_list:
            digit_number = (int)(num/postion) % 10
            queue_list[digit_number].append(num)

            if digit_number > 0 and is_loop:
                is_loop = False

        postion *= 10
        print(queue_list)

        index = 0

        for numbers in queue_list:
            for num in numbers:
                ordered_list[index] = num
                index += 1
        print("="*30+"ordered_list")
        print(ordered_list)



insert_number = int(input())
or_list = list()

for i in range(0, insert_number):
    or_list.append(int(input()))

print(or_list.pop(0))
print(or_list)