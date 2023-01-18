def solution(number, k):
    answer = ''
    col = []
    for i, num in enumerate(number) :
        while len(col) > 0 and col[-1] < num and k > 0 :
            col.pop()
            k = k - 1
        if k == 0 :
            col += list(number[i:])
            break
        col.append(num)
    if k > 0 :
        col = col[:-k]
    answer = ''.join(x for x in col)
    return answer