def solution(num_list):
    a = ''
    b = ''
    for x in num_list:
        if x%2==0:
            a += str(x)
        else:
            b += str(x)
    answer = int(a) + int(b)
            
    return answer