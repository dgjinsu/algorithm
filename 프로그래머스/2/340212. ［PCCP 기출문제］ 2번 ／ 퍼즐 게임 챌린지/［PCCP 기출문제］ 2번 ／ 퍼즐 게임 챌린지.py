def solution(diffs, times, limit):
    answer = 0
    
    def getSolveOnePuzzleTime(diff, level, time_cur, time_prev):
        if diff <= level:
            return time_cur
        else:
            return (time_cur + time_prev) * (diff - level) + time_cur
    
    def getSolveAllPuzzleTime(level):
        solve_time = 0
        for i in range(len(diffs)):
            if i == 0:
                solve_time += getSolveOnePuzzleTime(diffs[i], level, times[i], 0)
            else:
                solve_time += getSolveOnePuzzleTime(diffs[i], level, times[i], times[i-1])
        return solve_time
    
    left, right = 1, 300000
    
    while left <= right:
        mid = (left + right) // 2
        t = getSolveAllPuzzleTime(mid)
        if t <= limit:
            right = mid - 1
            answer = mid
        else:
            left = mid + 1
        
    return answer

# diff: 난이도
# time_cur: 퍼즐 소요 시간
# time_prev: 이전 퍼즐 소요 시간
# level: 숙련도

# diff <= level: 품
# diff > level: diff - level 만큼 재시도 => (time_cur + time_prev) * (diff - level) + time_cur

# 제한 시간 내에 퍼즐을 모두 해결하기 위한 "최소 숙련도"