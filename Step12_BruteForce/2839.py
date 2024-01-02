n = int(input())

a = n // 5
b = n % 5
answer = -1

while True:
    if a < 0:
        if n % 3 == 0:
            answer = n // 3
        break
    
    if b % 3 == 0:
        answer = a + b // 3
        break
    else:
        a -= 1
        b = n - 5 * a

print(answer)