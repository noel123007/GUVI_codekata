n1, k1 = input().split()
k1 = int(k1)
s1 = ''
if k1 == 0:
  print(int(n1))
elif k1 == len(n1):
  print(0)
else:
  n1 = list(map(int, list(str(n1))))
  for i1 in range(len(n1) - k1):
    s1 = s1 + str(min(n1[i1:k1+1]))
    n1.remove(min(n1[i1:k1+1]))
#     print(n)
  print(s1)
