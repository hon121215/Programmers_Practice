def solution(num_list):
    result = [x for x in range(len(num_list)) if num_list[x] < 0]
    if not result:
        result.append(-1)
    return result[0]
        
    
    