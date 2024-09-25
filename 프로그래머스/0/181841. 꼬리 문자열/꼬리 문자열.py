def solution(str_list, ex):
    answer = ''
    real_list = [x for x in str_list if ex not in x]
    for x in real_list:
        answer += x
    return answer