def solution(candy, positions):
    answer = []
    
    n_match, cache = 0, [0] *len(candy)
    
    for i in range(1, len(candy)) :
        # n_match가 1이상이고 서로 같은 문자가 아니라면 n_match를 이전으로 돌림
        while n_match and candy[n_match] != candy[i] :
            n_match = cache[n_match]
        # 문자가 일치한다면 n_match를 1증가시키고 cache에 매치하는 문자개수를 위치에 따라 넣음
        if candy[n_match] == candy[i] :
            n_match += 1
            cache[i] = n_match
    
    #일치하는 개수가 써져있는 cache를 슬라이스 하여 정답 계산
    for pos in positions:
        ans = 0
        while cache[pos-1]:
            #pos를 cache[pos-1]로 바꾸어 일치하는 문자가 있는지 확인하여 있다면 다시 while문 반복
            pos = cache[pos-1]
            ans += 1
        answer.append(ans)

        
    
    
    return answer