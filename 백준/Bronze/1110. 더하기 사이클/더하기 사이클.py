import sys

input = sys.stdin.readline
a = input().strip()
n = a
cnt = 0
while cnt <70 :
    word = []
    new_word=[]
    for i in a:
        word.append(int(i))
    if len(word) == 1:
        word.insert(0,0)
    new = sum(word)
    for i in str(new):
        new_word.append(i)
    if len(new_word) == 1:
         a = str(word[1]) + new_word[0]
    else:
        a = str(word[1]) + new_word[1]
    cnt += 1
    if int(n) == int(a):
        break
print(cnt)


