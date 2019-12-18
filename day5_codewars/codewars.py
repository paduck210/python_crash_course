def delete_nth(order, order_max):
    ans = []
    for ele in order:
        if ans.count(ele) < order_max: ans.append(ele)
    return ans

print(delete_nth([1,2,2,1,3,1], 2))


def delete_nth(order, max_e):
    ans = []
    for o in order:
        if ans.count(o) < max_e: ans.append(o)
    return ans

print(delete_nth([1,2,2,1,3,1], 2))
