n = int(input())

points = []

for _ in range(n):
    x, y = input().split()
    points.append((int(x), int(y)))

points = sorted(points)

for i in points:
    print(i[0], i[1])