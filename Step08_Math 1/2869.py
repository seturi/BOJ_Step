a, b, v = map(int, input().split())
days = (v - b) / (a - b)

if days == int(days):   # 낮 동안에 정상에 도착
    print(int(days))
else:           # 도착 못해서 미끄러짐, 하루 추가
    print(int(days) + 1)