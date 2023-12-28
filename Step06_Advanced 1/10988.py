s = input()
l = len(s)
answer = 1
for i in range(l//2):
    a, b = s[i], s[l - i - 1]
    if a != b:
        answer = 0
        break
print(answer)