N, M = list(map(int, input().split()))
value = list(map(int, input().split()))

length = len(value)
max_sum = 0

for i in range(0, length):
    for j in range(i + 1, length):
        for k in range(j + 1, length):
            sum_value = value[i] + value[j] + value[k]
            if sum_value <= M:
                max_sum = max(max_sum, sum_value)
print(max_sum)