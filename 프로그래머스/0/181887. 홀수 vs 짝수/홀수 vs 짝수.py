def solution(num_list):
    a = 0
    b = 0
    for x in range(len(num_list)):
        if x % 2 ==0:
            a += num_list[x]
        else:
            b += num_list[x]
    if a > b:
        return a
    else:
        return b