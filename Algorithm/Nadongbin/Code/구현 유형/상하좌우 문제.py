n = int(input())

x, y = 1, 1

plans = input().split()

# LRUD에 따른 이동 방향
dx = [0, 0, -1, 1]  # x축이 행을 의미 y축이 열을 의미
dy = [-1, 1, 0, 0]

move_types = ['L', 'R', 'U', 'D']

#이동 계획을 하나씩 확인하기

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
# 공간을 벗어나는 경우 무시
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x, y = nx, ny

print(x, y)
