#update
n = int(input())
num = input().split()
temp = []

for i in num:
    if num.count(i) > 1 and i not in temp:
        temp.append(i)
if len(temp) == 0:
    print('unique')
else:
    temp = sorted(temp)
    for i in temp:
        print(int(i),end=' ')
