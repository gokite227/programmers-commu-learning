def solution(storey):
    answer = []
    a = []
    b = []
    c = 0
    d = 0
    a.append(storey % 10)
    while storey > 10 :
        storey //= 10
        a.append(storey % 10)
    
    a.reverse()
    for i in a :
        i -= d
        c = 10-i
        print(i)
        if i > c :
            b.append(c)
            d = -1
        else :
            b.append(i)
            d = 0
    
    b[0] = a[0]+1
    answer.append(sum(a))
    answer.append(sum(b))
    print(a)
    print(b)
    print(answer)
    return min(answer)