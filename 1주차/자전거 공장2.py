order = [[3, 50], [7, 200], [8, 200]]
cost = [[0, 10], [50, 20], [100, 30], [200, 40]]

answer = 0
n = 0
product = []
for i in order :
    i[0] -= n
    n = i[0] + n

print(order)

for i in range(0,len(order)) :
    print(i)
    print(product)
    if len(product) > 0 :
        if order[i][1] / order[i][0] > order[i-1][1] / order[i-1][0] :
            product.append([order[i][0]+product[len(product)-1][0], order[i][1] + product[len(product)-1][1]])
            del product[len(product)-2]
    else :
        product.append(order[i])

for i, j in product :
    p_prev = 0
    for t, p in cost :
        if i * t >= j :
            break
        answer += (j - i * t) * (p - p_prev)
        p_prev = p
print(answer)


