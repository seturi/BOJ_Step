x = int(input())
y = int(input())
z = int(input())
sum = x + y + z

if x == y == z == 60:
    print("Equilateral")
elif sum == 180:
    if x == y or y == z or z == x:
        print("Isosceles")
    else:
        print("Scalene")
else:
    print("Error")