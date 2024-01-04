n = input()
result = list()

for i in range(len(n)):
    result.append(int(n[i]))

result.sort(reverse=True)

for i in result:
    print(i, end="")