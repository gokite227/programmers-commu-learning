def solution(number, k):
    answer = ''
    n_list = list(map(int, str(number)))
    remove_set = {10}
    a = 0
    for i in range(0,k) :
        if min(n_list) != 10 and min(n_list) :
            
            inx = n_list.index(min(n_list))
            n_list[inx] = 10
            

    result = [i for i in n_list if i not in remove_set]
    
    result = list(map(str,result))
    result = ''.join(s for s in result)
    
    return result