def solution(arr, n):
    answer = []
    if len(arr) % 2 == 0:
        for x in range(len(arr)):
            if x % 2 == 1:
                answer.append(arr[x] + n)
            else:
                answer.append(arr[x])
    elif len(arr) % 2 == 1:
        for x in range(len(arr)):
            if x % 2 == 0:
                answer.append(arr[x] + n)
            else:
                answer.append(arr[x])
                
    return answer