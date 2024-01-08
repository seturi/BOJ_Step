import sys

input = sys.stdin.readline

n, m = map(int, input().split())
a = list(input().strip() for _ in range(n))
b = list(input().strip() for _ in range(m))
c = list(set(a) & set(b))

c.sort()
cnt_c = len(c)
print(cnt_c)
for i in c:
    print(i)