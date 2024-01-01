a, b, c = map(int, input().split())

long = max(a, b, c)
not_long = a + b + c - long

if long < not_long:
    print(a+b+c)
else:
    print(not_long * 2 - 1)