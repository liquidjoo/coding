# radix sort
# queue_list = [list() for _ in range(10)]
#
# print(queue_list)


def radix_sort(ordered_list):
    is_sorted = False
    position = 1

    while not is_sorted:
        is_sorted = True
        queue_list = [list() for _ in range(10)]

        for num in ordered_list:
            digit_number = (int)(num / position) % 10
            queue_list[digit_number].append(num)


            # while true
            if is_sorted and digit_number > 0:
                is_sorted = False

        index = 0
        for numbers in queue_list:
            print(numbers)
            for num in numbers:
                ordered_list[index] = num
                index += 1

            print(ordered_list)

        position *= 10

    return ordered_list


insert_number = int(input())
or_list = list()

for i in range(0, insert_number):
    or_list.append(int(input()))

result = radix_sort(or_list)

# print(result)
