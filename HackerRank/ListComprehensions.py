import itertools

x =1
y =1
z=1
n=2


list_output = []

for element in itertools.product(range(x+1), range(y+1),range(z+1)):
    # print element
    if sum(element)!=n:
        print element
        list_output.append(element)

        print ('list_output', list_output)

