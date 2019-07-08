#update
s1, s2 = input().split()

temp = [0] * max(len(s2),len(s1))

for i in range(min(len(s2),len(s1))):
    if s1[i] == s2[i]:
        temp[i] = 1
print(temp.count(0))
