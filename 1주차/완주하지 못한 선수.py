def solution(participant, completion):
    dic = {}
    for i in participant :
        dic[i] = dic.get(i,0) + 1
    for i in completion :
        dic[i] = dic.get(i) - 1
    for key,value in dic.items() :
        if value == 1 :
            answer = key
    return answer