def solution(n):
    
    if n%2==1:
        result = 0
        for x in range(n+1):
            if x%2 ==1:
                result += x
        
    else:
        result = 0
        for x in range(n+1):
            if x%2==0 and x != 0:
                result += x**2
    
    return result