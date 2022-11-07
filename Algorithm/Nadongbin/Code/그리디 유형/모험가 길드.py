n = int(input())

data = list(map(int, input().split()))

data.sort()  # 기본 오름차순 정렬

result = 0  # 총그룹 수
count = 0  # 현재 그룹에 포함된 모험가 수

for i in data:
    count += 1
    if count >= i:  # 현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면, 그룹 결성
        result += 1  # 총 그룹 수 증가시키기
        count = 0  # 현재 그룹에 포함된 모험가 수 초기화

print(result)
