n = int(input())
num = sorted(input().split(), reverse=True)
temp = ''
for i in num:
    temp += i
print(int(temp))
