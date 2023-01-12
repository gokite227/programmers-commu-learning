def solution(cost, order)
    answer = 0
    limit = []
    cos = []
    month = []
    bike = 0
    limonth = 0
    n = 0

    for i in range(0,len(cost)) 
        limit.append(cost[i][0])
        cos.append(cost[i][1])
    del limit[0]
    
    
    for i in range(0,len(order)) 
        month.append(order[i][0])
        bike = bike + order[i][1]
    limonth = max(month)

    
        
    n = n -1
    answer = limonth  limit[0]  cos[0]
    print(answer)
    answer = answer + n  (limit[1] - limit[0])  cos[1]  
    print(answer)
    
    print(n)
    print(limit,cos)
    print(limonth,bike)
    return answer