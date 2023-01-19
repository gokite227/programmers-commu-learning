order = [[3, 50], [7, 200], [8, 200]]
cost = [[0, 10], [50, 20], [100, 30], [200, 40]]

answer = 0
n = 0
product = []
order.sort()
for i in order :
    i[0] -= n
    n = i[0] + n

for i,j in order :
    while product :
        _i, _j = product[-1]
        if i / j > _i / _j :
            break
        product.pop()
        i , j = i + _i , j + _j
    product.append([i, j])

for i, j in product :
    p_prev = 0
    for t, p in cost :
        if i * t >= j :
            break
        answer += (j - i * t) * (p - p_prev)
        p_prev = p

print(answer)


