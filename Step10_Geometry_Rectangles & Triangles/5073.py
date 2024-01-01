while True:
    side1, side2, side3 = map(int, input().split())
    if side1 == side2 == side3 == 0:
        break
    
    long = max(side1, side2, side3)
    if  long >= side1 + side2 + side3 - long:
        print("Invalid")
    elif side1 == side2 == side3:
        print("Equilateral")
    elif side1 == side2 or side2 == side3 or side3 == side1:
        print("Isosceles")
    else:
        print("Scalene")