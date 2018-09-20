if __name__ == '__main__':
    N = int(input())

    input_list = []
    for _ in range(N):
        operation = input()
        name, *line =operation.split(' ')
        scores = list(map(int, line))
        if 'insert' == name:
            input_list.insert(scores[0],scores[1])
        elif 'print' == name:
            print (input_list)
        elif 'remove' == name:
            input_list.remove(scores[0])
        elif 'append' == name:
            input_list.append(scores[0])
        elif 'sort' == name:
            input_list.sort()
        elif 'pop' == name:
            input_list.pop()
        elif 'reverse' == name:
            input_list.reverse()