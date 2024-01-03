import sys

n = int(sys.stdin.readline())
nums = [0] * 10001

for i in range(n):
    data = int(sys.stdin.readline())
    nums[data] += 1

for i in range(10001):
    if nums[i] != 0:
        for j in range(nums[i]):
            print(i)