def merge_sort_a(tmp_list):
    if len(tmp_list) <= 1:
        return tmp_list

    mid = len(tmp_list) // 2
    left_list = tmp_list[:mid]
    right_list = tmp_list[mid:]

    left_list = merge_sort_a(left_list)
    right_list = merge_sort_a(right_list)

    return merge_a(left_list, right_list)


def merge_a(left_list, right_list):
    result_list = list()

    while len(left_list) > 0 or len(right_list) > 0:
        if len(left_list) > 0 and len(right_list) > 0:

            if left_list[0] > right_list[0]:
                result_list.append(right_list[0])
                right_list = right_list[1:]

            else:
                result_list.append(left_list[0])
                left_list = left_list[1:]

        elif len(left_list) > 0:
            result_list.append(left_list[0])
            left_list = left_list[1:]

        elif len(right_list) > 0:
            result_list.append(right_list[0])
            right_list = right_list[1:]

    return result_list


insert_count = int(input())

arr = list()
for i in range(0, insert_count):
    arr.append(int(input()))


result = merge_sort_a(arr)

for j in range(0, insert_count):
    print(result[j])


