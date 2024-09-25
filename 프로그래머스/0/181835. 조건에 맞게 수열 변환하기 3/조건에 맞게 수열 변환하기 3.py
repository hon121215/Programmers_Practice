def solution(arr, k):
    answer = []
    for x in arr:
        if k % 2 == 0:
            answer.append(x+k)
        else:
            answer.append(x*k)
    return answer