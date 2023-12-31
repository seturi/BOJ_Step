while True:
    n = int(input())
    if n == -1:
        break
    divisor = []
    for i in range(1, n+1):
        if n % i == 0:
            divisor.append(i)
    if sum(divisor[:-1])!= n:
        print("%d is NOT perfect." % n)
    else:
        print("%d = 1" % n, end='')
        for div in divisor[1:-1]:
            print(" + %d" % div, end='')
        print()