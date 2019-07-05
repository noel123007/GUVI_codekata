n = int(input())
l = list(map(int, input().split()))
flag = 0
for i in range(len(l)-1):
    if sum(l[0:i+1])//(i+1) == sum(l[i+1:])//(len(l)-(i+1)):
        flag = 1
        break
if flag == 1:
    print("yes")
else:
    print("no")
        
