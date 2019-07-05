n = int(input())
num = list(map(int,input().split()))
temp = []
for i in range(n):
    if num[i] == i:
        temp.append(num[i])
if len(temp) == 0:
    print(-1)
else:
    for i in sorted(temp):
        print(i,end=' ')
        
