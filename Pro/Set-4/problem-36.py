n = int(input())
power = list(map(int,input().split()))
countt = 0
for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            if power[i] > power[j]:
                if power[j] > power[k]:
                    countt += 1

print(countt)
