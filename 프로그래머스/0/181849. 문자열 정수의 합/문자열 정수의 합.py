def solution(num_str):
    answer = 0
    ns = list(num_str)
    number = [int(x) for x in ns]
    answer += sum(number)
    return answer