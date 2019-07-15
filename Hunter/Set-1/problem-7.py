#update
n = int(input())
l = list(map(int,input().split()))

for i in range(len(l)):
    if i % 2 == 0 and l[i] % 2 == 1:
        print(l[i],end =' ')
    if i % 2 == 1 and l[i] % 2 == 0:
        print(l[i],end =' ')
