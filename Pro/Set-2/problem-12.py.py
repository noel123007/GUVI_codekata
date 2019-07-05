n, q = map(int,input().split())
l = list(map(int,input().split()))
for i in range(q):
    s, e = map(int,input().split())
    print(sum(l[s-1:e]))
    
