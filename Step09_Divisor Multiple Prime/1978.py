n = int(input())
cnt = 0
nums = list(map(int, input().split()))
for num in nums:
    if num == 1:
        continue
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        cnt += 1
print(cnt)