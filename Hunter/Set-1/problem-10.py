n, m = map(int,input().split())
l1 = list(map(int,input().split()))
l2 = list(map(int,input().split()))
flag = 1
for i in l2:
    if i not in l1:
        print('NO')
        flag = 0
        break
if flag == 1:
    print('YES')
