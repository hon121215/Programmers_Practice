def solution(num_list):
    x1 = 0
    x2 = 1
    for x in num_list:
        x1 += x
        x2 *= x
    if x2 < x1**2:
        return 1
    if x2 > x1**2:
        return 0