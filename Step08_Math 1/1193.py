n = int(input())

i = 1
group_nums = 1
prev_group_nums = 0
while n > group_nums:
    i += 1
    prev_group_nums = group_nums
    group_nums = i * (i + 1) // 2

n -= prev_group_nums
if i % 2 == 0:
    print("%d/%d" % (n, i + 1 - n))
else:
    print("%d/%d" % (i + 1 - n, n))