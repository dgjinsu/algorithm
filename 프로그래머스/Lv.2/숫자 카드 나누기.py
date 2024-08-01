import math
def solution(arrayA, arrayB):
    def gcd(x, y):
        a = max(x, y)
        b = min(x, y)
        if a % b == 0:
            return b
        return gcd(b, a % b)
    
    max_a = arrayA[0]
    max_b = arrayB[0]
    for i in arrayA[1:]:
        max_a = gcd(i, max_a)
        
    for i in arrayB[1:]:
        max_b = gcd(i, max_b)
        
    answer_a, answer_b = max_a, max_b
    
    for numA in arrayA:
        if numA % max_b == 0:
            answer_b = 0
            break
    for numB in arrayB:
        if numB % max_a == 0:
            answer_a = 0
            break
    
    return max(answer_a, answer_b)