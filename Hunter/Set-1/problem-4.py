n = int(input())
num = input().split()
for i in num:
    if num.count(i) == 1:
        print(i)
        break
