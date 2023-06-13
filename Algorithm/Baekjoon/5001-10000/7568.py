n = int(input())  # 전체 사람의 수 입력받기
people = []  # 각 사람의 덩치 정보를 저장할 리스트

# 각 사람의 몸무게와 키를 입력받아 리스트에 저장
for _ in range(n):
    weight, height = map(int, input().split())
    people.append((weight, height))

ranks = []  # 덩치 등수를 저장할 리스트

# 각 사람의 덩치 등수 계산
for i in range(n):
    rank = 1  # 초기 등수는 1로 설정
    for j in range(n):
        if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
            rank += 1
    ranks.append(rank)

# 결과 출력
print(' '.join(map(str, ranks)))





