def Euclid(x, y):
    while y != 0:
        x, y = y, x % y
    return x

a, b = map(int, input().split())
c, d = map(int, input().split())

m = a * d + c * b
n = b * d
gcd = Euclid(m, n)

print(m // gcd, n // gcd)