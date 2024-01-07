import bisect

n = int(input())
cards = list(map(int, input().split()))
m = int(input())
nums = list(map(int, input().split()))

# 1. 이분탐색
cards.sort()
for num in nums:
    left = bisect.bisect_left(cards, num)
    right = bisect.bisect_right(cards, num)
    print(right - left, end=' ')

# 2. 딕셔너리 탐색
dict = {}
for num in nums:
    dict[num] = 0

for card in cards:
    if card in dict:
        dict[card] = 1

for i in dict:
    print(dict[i], end=' ')