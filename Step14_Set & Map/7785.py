n = int(input())

dict = {}
for _ in range(n):
    name, status = input().split()
    if status == "enter":
        dict[name] = 1
    elif status == "leave":
        del dict[name]
        
dict = sorted(dict.keys(), reverse=True)
for i in dict:
    print(i)