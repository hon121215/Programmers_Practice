def solution(s1, s2):
    return len([(a,b) for a in s1 for b in s2 if a == b])