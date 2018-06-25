data = input().lower()
alphabet_list = [0 for k in range(ord('a')-97, ord('z')-96)]
for i in range(int(data.__len__())):
    index = ord(data[i])-97
    alphabet_list[index] += 1

max_v = max(alphabet_list)
max_count = 0
for j in range(26):
    if alphabet_list[j] == max_v:
        max_count += 1

if max_count >= 2:
    print("?")
else:
    print(chr(alphabet_list.index(max(alphabet_list)) + 97).upper())
