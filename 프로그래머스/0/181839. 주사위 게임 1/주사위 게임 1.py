def solution(a, b):
    answer = 0
    if a % 2 == 1 and b % 2 == 1:
        sum_num = a**2 + b**2
        answer += sum_num
    elif a % 2 == 1 or b % 2 == 1:
        sum_num = 2*(a+b)
        answer += sum_num
    else:
        sum_num = abs(a-b)
        answer += sum_num
    
    
    
    return answer