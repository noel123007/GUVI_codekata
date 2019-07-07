n = int(input())
l = input().split()
flag = 0
for i in l:
  if l.count(i) > 1:
    print(int(i))
    flag = 1
    break
    
if flag == 0:
  print("unique")
