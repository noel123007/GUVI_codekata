#update
s = list(input().lower())
s = set(s)
if ' ' in s:
    s.remove(' ')

if len(s) == 26:
    print('yes')
else:
    print('no')
