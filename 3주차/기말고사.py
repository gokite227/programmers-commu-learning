def solution(t, k, study, pstudy):
    answer = 0
    p_time = []
    for i in range(k) :
        if t - min(pstudy) < 0 :
            break
        else :
            answer += 1
            t -= min(pstudy)
            pstudy.remove(min(pstudy))
    
    print(t)

    while True :
        if t - min(study) < 0 :
            break
        else :
            answer += 1
            t -= min(study)
            study.remove(min(study))
    
    return answer