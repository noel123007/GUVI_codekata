n = int(input())
l = list(map(int, input().split()))
maximum = 0
cnt = 0
for i in range(n-1):
    if l[i] < l[i+1]:
        cnt +=1
        if maximum < cnt:
            maximum = cnt
    else:
        cnt = 0
print(maximum+1)
        
        
