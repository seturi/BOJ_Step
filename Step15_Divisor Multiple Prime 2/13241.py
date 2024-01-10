a, b = map(int, input().split())
c = a * b
while b != 0: # 유클리드 호제법
    r = a % b
    a = b
    b = r
print(c // a)