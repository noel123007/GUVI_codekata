n, k = input().split()
k = int(k)
s = ''
if k == 0:
  print(int(n))
elif k == len(n):
  print(0)
else:
  n = list(map(int, list(str(n))))
  for i in range(len(n) - k):
    s = s + str(min(n[i:k+1]))
    n.remove(min(n[i:k+1]))
    print(n)
  print(s)
