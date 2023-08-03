import sys

w, n = map(int,sys.stdin.readline().split())

# 금속의 종류와 가격을 입력받을때, n만큼 반복문을 돌면 절대안된다.
# n만큼 반복문을 돌면 시간복잡도가 O(N)이 나와서 시간초과가 된다.
# 무조건 리스트컴프리핸션으로 풀기

jewels = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

jewels.sort(key=lambda x: x[1], reverse=True)


# jewels = [ [70,2] , [90,1] ]
answer = 0
for weight, price in jewels:
    if w > weight:
        answer += weight * price
        w -= weight
    else:
        answer += w * price
        break

sys.stdout.write(str(answer))