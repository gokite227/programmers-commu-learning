def solution(scoville, K):
    #answer
    answer = 0
    s_coville = scoville
    f = 0
    s = 0
    for i in scoville :
        print(i)
        if len(scoville) == 1 and scoville[0] < k :
            answer = -1
            break
        if i < K :
            answer += 1
            f = min(scoville)
            scoville.remove(f)
            s = min(scoville)
            scoville.remove(s)
            scoville.append(f + (s*2))
    
    return answer