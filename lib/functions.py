import math

def divisors(t_number):
    divisors_num = 0
    div = list(range(1,int(math.ceil(math.sqrt(t_number)+1))))
    print div

    for i in div:
        if t_number%i == 0:

            divisors_num = divisors_num + 2


    return divisors_num

print divisors(10)