N, B = map(int, input().split())
number = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
answer = ""

while N:
    i = N % B
    N //= B
    answer += number[i]

print(answer[::-1])