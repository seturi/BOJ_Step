n = int(input())
count = 0
answer = 666

while True:
    if '666' in str(answer):
        count += 1
    if count == n:
        break
    answer += 1

print(answer)