#update
n = int(input())
power = list(map(int,input().split()))
countt = 0
for i in range(len(power)-2):
    for j in range(i+1,len(power)-1):
        for k in range(j+1,len(power)):
            if power[i] > power[j]:
                if power[j] > power[k]:
                    countt += 1

print(countt)
