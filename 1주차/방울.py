def solution(bell):
    answer = 0
    dic = {}
    dic1 = {}
    arr = []
    rebell = []
    rebell = bell[::-1]

    for i in bell :
        dic[i] = dic.get(i,0) + 1
        
        if dic.get(1) == dic.get(2):
            arr.append(dic.get(1) + dic.get(2))
            
    dic1 = dic.copy()
    
    for i in range(0,len(bell)) :
        dic[bell[i]] = dic.get(bell[i],0) - 1
        if dic.get(1) == dic.get(2):
            arr.append(dic.get(1) + dic.get(2))   
        # dic[rebell[i]] = dic.get(rebell[i],0) - 1
        # if dic.get(1) == dic.get(2):
        #     arr.append(dic.get(1) + dic.get(2))
        
        
    for i in rebell :
        dic1[i] = dic1.get(i,0) - 1
        if dic1.get(1) == dic1.get(2):
            arr.append(dic1.get(1) + dic1.get(2))
            
    
    try : 
        answer = max(arr)
    except:
        answer = 0
    return answer