a = input()
wordlist = [-1 for k in range(ord('a')-97, ord('z')-96)]

for i in range(int(a.__len__())):
    index = ord(a[i]) - 97
    if wordlist[index] == -1:
        wordlist[index] = i

for j in range(int(wordlist.__len__())):
    print(wordlist[j], end=" ")
