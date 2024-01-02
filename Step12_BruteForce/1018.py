n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]
count = []

for i in range(n-7):
    for j in range(m-7):
        paint_w = 0
        paint_b = 0
        for a in range(i, i+8):
            for b in range(j, j+8):
                if (a+b) % 2 == 0:
                    if board[a][b] != "W":
                        paint_w += 1
                    if board[a][b] != "B":
                        paint_b += 1
                else:
                    if board[a][b] != "W":
                        paint_b += 1
                    if board[a][b] != "B":
                        paint_w += 1

        count.append(min(paint_w, paint_b))
        
print(min(count))