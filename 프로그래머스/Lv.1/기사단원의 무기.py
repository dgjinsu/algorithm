def solution(number, limit, power):
    # 약수 개수에 해당하는 공력력 무기
    # 제한 수치 보다 크면 협약기관에서 정한 공격력 무기 구매
    # 공격력 1 -> 철 1
    answer = 0
    
    def getPower(n):
        cnt = 0
        for i in range(1, int((n ** 0.5) + 1)):
            if n % i == 0:
                if i == (n // i):
                    cnt += 1
                else:
                    cnt += 2
                if cnt > limit:
                    return power
        return cnt
    
    tmp = []
    for n in range(1, number + 1):
        tmp.append(getPower(n))
    return sum(tmp)