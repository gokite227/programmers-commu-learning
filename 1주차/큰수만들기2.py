def solution(number, k):
    answer = ''
    number = [str(x) for x in number]
    num = [number[0]]
    for i in range(1,len(number)) :
        
        if number[i] > number[i-1] and k > 0 :
                del num[len(num)-1]
                k = k -1
                num.append(number[i])
        else :   
            num.append(number[i])

    return answer