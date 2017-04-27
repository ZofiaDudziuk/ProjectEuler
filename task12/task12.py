import math
def triangular(counter):

    if (counter*(counter+1))%2 == 0:
        t_number = (counter*(counter+1))/2

        # print t_number
        return t_number
    else:
        return t_number

        # print y



def divisors(t_number):
    divisors_num = 0
    div = list(range(1,int(math.ceil(math.sqrt(t_number)+1))))
    # print div

    for i in div:
        if t_number%i == 0:

            divisors_num = divisors_num + 2


    return divisors_num



        # print 'mod', mod
        # if mod == 0:
        #     div_list.append(i)
        #     print div_list
        #     length =  len(div_list)
        #     print 'length', length
        #     return length


for counter in range(500,100000):
    y =triangular(counter)
    x =divisors (y)
    if x > 500:

        print y
        break


# x= triangular()
# print divisors(x)