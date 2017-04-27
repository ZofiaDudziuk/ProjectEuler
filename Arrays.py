import numpy

test_array = numpy.arange(30).reshape(3,10)
##print test_array

##for line in test_array:
##    print line
##    for item in range(len(line)):
##        if item < 7:
##            print "item", item
##            
##            a = line[item] + line[item+1] + line [item +2] + line [item +3]
##            print a

b =10
c = b- 3

def sum_func(line):
    for item in range(len(line)):
        print line
        if item < c:
            max_sum = 0
            a = line[item] + line[item+1] + line[item +2] + line[item +3]
##            print a
##            return a
##        else:
##            break
            if max_sum < a:
                max_sum = a
                print max_sum
    return max_sum

test =numpy.apply_along_axis(sum_func, 1, test_array)
print test
