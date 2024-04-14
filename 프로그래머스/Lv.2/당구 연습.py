def solution(m, n, startX, startY, balls):
    # m: 가로
    # n: 세로
    answer = []
    
    # 어디 벽으로 박을지
    for ball in balls:
        b = [] # 바닥, 천장, 왼, 오
        if not(startX == ball[0] and startY > ball[1]):
            d2 = (ball[0] - startX)**2 + (ball[1] + startY)**2 # 바닥
            b.append(d2)
            
        if not(startX == ball[0] and startY < ball[1]):
            d2 = (ball[0] - startX)**2 + (ball[1] - (2*(n-startY) + startY))**2 # 천장
            b.append(d2)
            
        if not(startY == ball[1] and startX > ball[0]):
            d2 = (ball[0] + startX)**2 + (ball[1] - startY)**2 # 왼
            b.append(d2)
            
        if not(startY == ball[1] and startX < ball[0]):
            d2 = (ball[0] - (2*(m-startX) + startX))**2 + (ball[1] - startY)**2
            b.append(d2) # 오
            
        answer.append(min(b))
    
    return answer