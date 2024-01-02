n = int(input())
for num in range(n):
    sum = num
    str_num = str(num)
    for i in str_num:
        sum += int(i)
    if sum == n:
        print(num)
        break
else:
    print(0)