import heapq

def solution(t, k, study, pstudy):
    answer = 0
    
    heapq.heapify(pstudy)
    
    for i in range(k) :
        min1 = heapq.heappop(pstudy)
        study.append(min1) 
    heapq.heapify(study)
    while True :
        min2 = heapq.heappop(study)
        if t >= min2 :
            t -= min2
            answer += 1
        else :
            break 
    return answer