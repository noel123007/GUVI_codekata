class Node:
    def __init__(self,data):
        self.data = data
        self.child = []
        
n = int(input())
node = [None]*(n+1)
visited = []
temp = []

for i in range(n-1):
    s1, s2 = list(map(int,input().split()))
    temp.append([s1,s2])
    if s1 not in visited:
        node[s1] = Node(s1)
        visited.append(s1)
    if s2 not in visited:
        node[s2] = Node(s2)
        visited.append(s2)

visited = [1]
for i in range(len(temp)):
    if temp[i][0] in visited:
        node[temp[i][0]].child.append(node[temp[i][1]])
        visited.append(temp[i][1])
    else:
        node[temp[i][1]].child.append(node[temp[i][0]])
        visited.append(temp[i][0])

root = node[1]
queue = [root]
level = 1

while(len(queue) >0): 

    n = len(queue) 
    while(n > 0) : 
        p = queue[0] 
        queue.pop(0) 

        if level % 2 == 1:
            print(p.data,end=' ')
            
        for index, value in enumerate(p.child): 
            queue.append(value) 

        n -= 1
    level += 1
    
