m = int(input())
n = int(input())

prime = []
for num in range(m, n+1):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            prime.append(num)

if len(prime) == 0:
    print(-1)
else:
    print(sum(prime))
    print(min(prime))