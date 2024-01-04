import sys

input = sys.stdin.readline
n = int(input())
points = list(map(int, input().split()))
unique_pts = sorted(list(set(points)))

dict = {unique_pts[i]: i for i in range(len(unique_pts))}

for i in points:
    print(dict[i], end=' ')