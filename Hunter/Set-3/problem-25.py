class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def search(root, data,path):
    path.append(root.data)
    if root == None or root.data == data:
        return path
    if data < root.data:
        return search(root.left, data,path)
    else:
        return  search(root.right, data,path)
   
def insert(root,node): 
    if root is None: 
        root = node 
    else: 
        if root.data < node.data: 
            if root.right is None: 
                root.right = node 
            else: 
                insert(root.right, node) 
        else: 
            if root.left is None: 
                root.left = node 
            else: 
                insert(root.left, node)

n = int(input())
l = list(map(int,input().split()))
u, v = map(int,input().split())
path = []
root = Node(l[0])
for i in range(1,len(l)):
    insert(root, Node(l[i]))

path_u = search(root,u,[])
path_v = search(root,v,[])
u = len(path_u)
v = len(path_v)
flag = 0
for i in range(min(u,v)):
    if path_u[i] != path_v[i]:
        if u < v:
            print(path_u[i-1])
        else:
            print(path_v[i-1])
        flag = 1
        break
if flag == 0:
    if u < v:
        print(path_u[-1])
    else:
        print(path_v[-1])
