N, B = input().split()
number = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
B = int(B)
answer = 0
l = len(N)
for i in range(l):
    answer += (B ** i) * number.find(N[l-i-1])

print(answer)