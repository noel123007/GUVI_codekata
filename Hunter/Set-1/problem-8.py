n = int(input())
l = list(map(int,input().split()))

for i in range(0,len(l)-2):
    for j in range(i + 1, len(l)-1):
        if (l[i] + l[j]) in l[j + 1:]:
            print(l[i], l[j], l[i] + l[j])
        
