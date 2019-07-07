import math

x1, y1 = map(int,input().split())
x2, y2 = map(int,input().split())
x3, y3 = map(int,input().split())
x4, y4 = map(int,input().split())

l = [[x1,y1],[x2,y2],[x3,y3],[x4,y4]]
temp = []
for i in range(len(l)-1):
    for j in range(i+1,len(l)):
        c = math.sqrt(abs(l[i][1] - l[j][1])**2 + abs(l[i][0] - l[j][0])**2)
        temp.append(c)
temp = sorted(temp)
temp = [str(i) for i in temp]
if temp.count(temp[0]) == 4 and temp.count(temp[-1]) == 2:
    print('yes')
else:
    print('no')
