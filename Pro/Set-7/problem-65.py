n, k = map(int,input().split())
cost = list(map(int,input().split()))
b = int(input())

s = sum(cost)
a = s - cost[k]

if b == a//2:
    print("Bon Appetit")
else:
    print(b-a//2)
