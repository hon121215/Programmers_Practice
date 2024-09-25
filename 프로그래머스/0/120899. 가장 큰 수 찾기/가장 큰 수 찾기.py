def solution(array):
    result = []
    result.append(max(array))
    result.append(array.index(max(array)))
    
    return result