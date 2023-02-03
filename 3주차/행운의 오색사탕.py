def solution(candy, positions):
    answer = []
    for i in positions:
        candy1 = candy[:i]
        n = 1
        ans1 = 0
        if i == 1 :
            answer.append(0)
        else  :
            while n * 2 <= i + 1 :
                if candy1[:n] == candy1[-n:] :
                    ans1 += 1
                n += 1
            answer.append(ans1)
    return answer