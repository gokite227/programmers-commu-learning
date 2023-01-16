def solution(numbers):
    answer = ''
    max_list = []
    an = []
    max_len = 0
    numbers = reversed(sorted(numbers))
    for i in numbers :
        num_list = list(map(int,str(i)))
        max_list.append(num_list)
        if len(num_list) > max_len :
            max_len = len(num_list)
    for i in range(0,len(max_list)) :
        # print(max(max_list[i:len(max_list)]))
        a= max(max_list[i:len(max_list)])
        an.append(a)
        max_list.insert(0,a)
        max_list[inx] = 0
        print(max_list)
        print(a)
        # print(max(max_list[i:len(max_list)]))
         
        # for j in range(0,max_len) :

    return answer