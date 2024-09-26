def solution(numLog):
    answer = ''
    for x in range(len(numLog)-1):
        if numLog[x] - numLog[x+1] == -1:
            answer += 'w'
        elif numLog[x] - numLog[x+1] == 1:
            answer += 's'
        elif numLog[x] - numLog[x+1] == -10:
            answer += 'd'
        elif numLog[x] - numLog[x+1] == 10:
            answer += 'a'
        
    return answer