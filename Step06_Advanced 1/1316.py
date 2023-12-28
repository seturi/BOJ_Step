n = int(input())
answer = 0
for _ in range(n):
    s = input()
    group = []
    for i in s:
        if i not in group:
            group.append(i)
        elif group[-1] != i:
            break
    else:
        answer += 1
            
print(answer)