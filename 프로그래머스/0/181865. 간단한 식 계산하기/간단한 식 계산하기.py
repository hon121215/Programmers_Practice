def solution(binomial):
    answer = 0
    result = [x for x in binomial.split()]
    if result[1] == '+':
        answer = int(result[0]) + int(result[2])
    elif result[1] == '-':
        answer = int(result[0]) - int(result[2])
    else:
        answer = int(result[0]) * int(result[2])
    return answer