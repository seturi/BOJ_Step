s = input()
croatia = ['c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z=']
answer = 0
cur = 0

while (cur < len(s)):
    if s[cur:cur+2] in croatia:
        cur += 2
    elif s[cur:cur+3] == 'dz=':
        cur += 3
    else:
        cur += 1
    answer += 1

print(answer)