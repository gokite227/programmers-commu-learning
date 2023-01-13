def solution(n, lost, reserve):
    answer = n
    a = len(lost)
    inx = 0
    print("*",n)
    for i in lost :
        for j in reserve :
            print("--",i,j)

            if i == j :
                inx = reserve.index(j)
                reserve[inx] = -1
                a = a - 1
                print("r",n)   

            elif i == j + 1 :
                inx = reserve.index(j)
                reserve[inx] = -1
                a = a - 1
                print(i,j,"+",n) 

            elif i == j - 1 :
                inx = reserve.index(j)
                reserve[inx] = -1
                a = a - 1
                print(i,j,"-", n)
        inx = lost.index(i)
        lost[inx] = -1
        
    answer = answer - a    

    if n < answer :
        answer = n
            
    return answer