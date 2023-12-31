n = int(input())

layer = 0
while n > 1:
    layer += 1
    n -= 6 * layer
print(layer + 1)