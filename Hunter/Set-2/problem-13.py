s = input()

stack = []

for i in s:
    stack.append(i)

if s == ''.join([x for x in s[::-1]]):
    print('YES')
else:
    print('NO')
