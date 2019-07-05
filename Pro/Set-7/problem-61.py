s1 = input()
s2 = input()
temp = ''
l = [chr(i) for i in range(97,123)]
count = 0
for i in range(len(s2)):
    s2_index = l.index(s2[i]) + 1
    s1_index = l.index(s1[i]) + 1
    if s1_index + s2_index > 26:
        pos = s1_index - (26 - s2_index)
        temp += l[pos-1]
        #print(l[pos-1],1)
    else:
        pos = s1_index + s2_index
        temp += l[pos-1]
        #print(l[pos-1],2)
print(temp)
