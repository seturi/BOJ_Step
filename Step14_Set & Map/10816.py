import sys

input = sys.stdin.readline

n = int(input())
cards = list(map(int, input().split()))
m = int(input())
nums = list(map(int, input().split()))

dict = {}
for card in cards:
    if card in dict:
        dict[card] += 1
    else:
        dict[card] = 1

for num in nums:
    if num in dict:
        print(dict[num], end=' ')
    else:
        print(0, end=' ')