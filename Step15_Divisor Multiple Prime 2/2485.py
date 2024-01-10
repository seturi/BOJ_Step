import sys
import math

input = sys.stdin.readline

n = int(input())
prev = int(input())
gaps = []
for _ in range(n-1):
    tree = int(input())
    gaps.append(tree - prev)
    prev = tree

gcd = gaps[0]
for gap in gaps:
    gcd = math.gcd(gcd, gap)

answer = 0
for gap in gaps:
    answer += gap // gcd - 1

print(answer)