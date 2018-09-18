import itertools
from operator import itemgetter

if __name__ == '__main__':

    list_students = []
    sublist = []
    final_list = []

# puts input in the list of lists
    for _ in range(int(input())):
        sublist = []
        name = input()
        score = float(input())
        sublist.append(name)
        sublist.append(score)

        list_students.append(sublist)

# sorts list by values
    list_students.sort(key=itemgetter(1))

# finds the min score
    first_value = None
    for item in itertools.chain(list_students):
        if first_value is None:
            first_value = item[1]

#finds the second lowest score
    second_low = 0
    for item in itertools.chain(list_students):
        if item[1]>first_value:
            second_low = item[1]
            break
        else:
            pass
#creats a list with the students that had the secon lowest score
    for item in itertools.chain(list_students):

        if item[1]==second_low:
            final_list.append(item[0])

# sorts the list alphabeticaly and prots the names
    final_list.sort()

    for item in final_list:
        print (item)