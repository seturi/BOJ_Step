n, m = map(int, input().split())
s = list(input() for _ in range(n))
check = list(input() for _ in range(m))

dict = {}
for i in s:
    dict[i] = 0

answer = 0
for i in check:
    if i in dict:
        answer += 1

print(answer)