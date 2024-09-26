def solution(numbers, direction):
    result = []
    if direction == 'right':
        result.append(numbers[-1])
        for x in range(len(numbers)-1):
            result.append(numbers[x])
    elif direction == 'left':
        for x in range(1,len(numbers)):
            result.append(numbers[x])
        result.append(numbers[0])
        
    return result
        