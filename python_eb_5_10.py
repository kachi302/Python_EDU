# n, m 을 공백으로 구분하여 입력받기
n, m = map(int, input('배열의 크기는 ').split())

#2차원 리스트의 맵 정보 입력 받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))
    
# DFS 로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문
def dfs(x, y):
    # 주어진 범위에서 벗어나는 경우에는 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    # 현재 노드를 방문하지 않았다면,
    if graph[x][y] == 0:
        # 해당 노드 방문 처리
        graph[x][y] = 1
        # 상, 하, 좌, 우의 모든 재귀적 호출
        dfs(x-1, y)
        dfs(x, y -1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False
result = 0
for i in range(n):
    for j in range(m):
        #현재 위치에서 DFS 수행
        if dfs(i, j) == True:
            result += 1
print(result) # 정답 출력            
            