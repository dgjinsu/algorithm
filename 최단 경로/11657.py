import sys
import heapq as hq
input = sys.stdin.readline
INF = int(10e9)

n, m = map(int, input().split())
graph = []
dis = [INF] * (n + 1)
isPossible = True

for _ in range(m):
    a, b, c = map(int, input().split())
    graph.append((a, b, c))

def bellman_ford(start):
    dis[start] = 0

    # n번의 라운드를 반복
    for i in range(1, n + 1):
        # 매 라운드마다 모든 간선을 확인
        for j in range(m):
            now, next, cost = graph[j][0], graph[j][1], graph[j][2]
            # 현재 간선을 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if dis[now] != INF and dis[next] > dis[now] + cost:
                dis[next] = dis[now] + cost
                # n번째 라운드에서도 값이 갱신된다면 음수 순환 존재
                if i == n:
                    return True

    return False

answer = bellman_ford(1)
if answer:
    print(-1)
else:
    for i in range(2, n+1):
        if dis[i] == INF:
            print(-1)
        else:
            print(dis[i])

#다익스트라 시도 실패
#음수 간선이 포함된 상황에선 밸만포드 알고리즘을 사용해야 함
# import sys
# import heapq as hq
# input = sys.stdin.readline
# INF = int(10e9)

# n, m = map(int, input().split())
# graph = [[] for _ in range(n + 1)]
# for i in range(m):
#   A, B, C = map(int, input().split())
#   graph[A].append((B, C))

# def dijksta(start):
#   dis = [INF] * (n + 1)
#   dis[start] = 0
#   q = []
#   hq.heappush(q, (0, start))
#   while q:
#     dist, now_node = hq.heappop(q)
#     for n_n, weight in graph[now_node]:
#       cost = dist + weight
#       if dis[n_n] > cost:
#         dis[n_n] = cost
#         hq.heappush(q, (cost, n_n))
#     count = 0
#     for i in range(1, len(dis)):
#       if dis[i] < 0:
#         count += 1
#     if count == n:
#       print(-1)
#       exit()
#   return dis

# answer = dijksta(1)
# for i in range(2, len(answer)):
#   if answer[i] == INF:
#     print(-1)
#   else:
#     print(answer[i])