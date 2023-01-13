# 방법1
def solution(n, lost, reserve):
    answer = []
    a = 0
    s = []
    s1 = []
    for i in range(1,n+1) :
        s.append(1)
    s.append(1)
    s.insert(0, 1)
    for i in reserve :
        s[i] = 2
    for i in lost :
        s[i] = s[i] - 1
    s1 =  s.copy()   
    for i in range(0,len(s)) :
        if s[i] == 2 and s[i-1] == 0:
            s[i] = 1
            s[i-1] = 1
        elif s[i] == 2 and s[i+1] == 0:
            s[i] = 1
            s[i+1] = 1
    answer = (s.count(1)+s.count(2)) - 2
    

    
    return answer

# 방법2

def solution(n, lost, reserve):
    answer = 0
    s = set(lost) & set(reserve)
    l = set(lost) - s
    r = set(reserve) -s
    
    for i in r :
        if i - 1 in l :
            l.remove(i-1)
        elif i + 1 in l :
            l.remove(i+1)
    answer = n - len(l)
            
    return answer