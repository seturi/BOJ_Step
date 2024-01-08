import sys

input = sys.stdin.readline

n, m = map(int, input().split())
dict = {}
for i in range(1, n+1):
    pokemon = input().strip()
    dict[pokemon] = i
    dict[i] = pokemon

for _ in range(m):
    quiz = input().strip()
    if quiz.isdigit():
        print(dict[int(quiz)])
    else:
        print(dict[quiz])