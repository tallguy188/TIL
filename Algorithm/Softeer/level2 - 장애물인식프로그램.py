import sys
from collections import deque

input = sys.stdin.readline
print = sys.stdout.write

n = int(input())

graph = []

for i in range(n):
    graph.append(list(map(int,input().strip())))


count_list = []
def dfs(x,y):
    if x<=-1 or x>=n or y<=-1 or y>=n:
        return False

    global count

    if graph[x][y] == 1:
        graph[x][y] =0      # 방문완료처리를 하지 않으면 dfs가 무한히 호출된다.

        count +=1
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        # 깊이우선탐색으로 재귀호출을 사용
        return True
    return False
# 블록 별 개수
result = 0
for i in range(n):
    for j in range(n):
        count= 0
        if dfs(i,j) == True:
            result +=1
            count_list.append(count)
count_list.sort()
print(str(result) + '\n')
for k in count_list:
    print(str(k) + '\n')







