table = [list(map(int, input().split())) for _ in range(9)]

answer = table[0][0]
x, y = 0, 0

for i in range(9):
    for j in range(9):
        if answer < table[i][j]:
            x, y = i, j
            answer = table[i][j]

print(answer)
print(x + 1, y + 1)