n = int(input())
l = []
for i in range(n):
    l.append(input())

temp = [len(x) for x in l]
pos = temp.index(min(temp))
temp = l[pos]
l.remove(l[pos])

def substring(s):
    global temp, l
    count = 0
    #print(temp)
    for i in range(len(temp)):
        if temp[i] != s[i]:
            return count
        else:
            count += 1
    return count
#print(l)
lst = list(map(substring, l))
#print(lst)
print(temp[0:max(lst)])
