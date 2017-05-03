import math

def getNumberOfDivisors(n):
    divisorsCount = 0
    div = list(range(1, int(math.ceil(math.sqrt(n) + 1))))

    for i in div:
        if n%i == 0:
            result = n / i
            if i == result:
                divisorsCount = divisorsCount + 1
            else:
                divisorsCount = divisorsCount + 2


    return divisorsCount

