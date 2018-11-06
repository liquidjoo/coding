"""
정육면체 6
[1], [2,3,4,5,6,7], [8,9,10,11,12,13,14,15,16,17,18,19], [20~ 37 ],
1       6             12

1, 2, 8, 20, 38, 62

  1 6 12 18 24


1 6n






8



1  2  3   4  5   6


58 // 6

"""
a = input()
a = int(a)
index = 0
number = 1
while True:

    if a < number:
        print(index)
        break
    else:
        if number == 1:
            number += 1
        else:
            number = number + (index * 6)
        index += 1













