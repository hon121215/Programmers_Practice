def solution(n):
    answer = []
    for x in range(n):
        n_array = [0]*n
        answer.append(n_array)
        answer[x][x] = 1
    return answer