def solution(storey):
    answer = []
    a = []
    b = []
    a.append(storey % 10)
    while storey > 10 :
        storey //= 10
        a.append(storey % 10)
    a.reverse()
    for i in a :
        b.append(10-i)
    b[0] = a[0]+1
    answer.append(sum(a))
    answer.append(sum(b))
    print(a)
    print(b)
    print(answer)
    return min(answer)