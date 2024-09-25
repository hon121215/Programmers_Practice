def solution(num_list, n):
    answer = []
    answer += [x for x in num_list[::n]]
    return answer