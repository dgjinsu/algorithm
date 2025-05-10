def solution(n, w, num):
    boxes = [0] * w
    for i in range(0, n):
        if (i // w) % 2 == 0:
            boxes[i % w] += 1
        else:
            boxes[w - i % w - 1] += 1
    
    idx = (num - 1) % w
    
    # 층 / 홀수: 정방향  짝수층: w - 1 - idx
    h = (num - 1) // w + 1

    if h % 2 == 0:
        idx = w - 1 - idx
    
    return boxes[idx] - h + 1