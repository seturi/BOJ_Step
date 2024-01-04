import sys

input = sys.stdin.readline
n = int(input())
words = []

for _ in range(n):
    words.append(input().strip())
    
words = list(set(words))
words.sort()
words.sort(key=len)

for word in words:
    print(word)