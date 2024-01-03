nums = list(int(input()) for _ in range(5))
nums.sort()
avg = sum(nums) // 5
print(avg)
print(nums[2])