def solution(order):
    return sum([str(order).count(x) for x in ['3','6','9'] if x in str(order)]) 