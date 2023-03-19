# n,m을 입력받음

n,m = map(int,input().split())

#방문한 위치를 저장하기 위한 맵을 생성, 0으로 초기화

d = [[0] *m for _ in range(n)]

#현재 x좌표, y좌표, 방향 입력받기
x,y, direction = map(int,input().split())

#전체 맵 정보 입력

array = []

for i in range(n):
    array.append(list(map(int,input().split())))


# 북,동,남,서 방향정의
dx = [-1,0,1,0]
dy = [0,1,0,-1]

#회전함수

def turn_left():
    global direction
    direction -1 = direction
    if direction == -1:
        direction = 3



count = 1
turn_time= 0

while True:
    turn_left() #왼쪽으로 회전
    nx = x + dx[direction]
    ny = y + dy[direction]

    if d[nx][ny]== 0 and array[nx][ny] == 0:
        d[nx][ny] ==1
        x = nx
        y = ny
        count += 1
        turn_time=0
        continue # 이동한 다음 다시 조건을 따져봐야되므로 continue

    else :       # 회전한 이후 정면이 가본칸이거나 바다인경우
        turn_time +=1

    if turn_time == 4:   #네방향 모두 갈수없는 경우
        nx = x-dx[direction]
        ny = y-dy[direction]
        #뒤로갈수있으면 이동
        if array[nx][ny] ==0:
            x =nx
            y = ny

        #뒤가 바다인경우
        else:
            break
        turn_time = 0

print(count)
