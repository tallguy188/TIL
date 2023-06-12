"""
세준이는 기말고사를 망쳤다. 세준이는 점수를 조작해서 집에 가져가기로한다. 일단 세준이는 자기 점수 중에 최댓값을 골랐다. 이 값을 M이라고 한다. 
그리고 나서 모든 점수를 점수/M*100으로 고쳤다. 
예를 들어 세준이의 최고점은 70이고, 수학점수가 50이었으면 수학점수는 50/70*100이 되어 71.43점이 된다. 
세준이의 성적을 위 방법으로 계산했을 때, 새로운 평균을 구하는 프로그램을 작성하시오.
"""





m = int(input())

lst = list(map(int,input().split()))


for i in range(len(lst)-1):
	max = lst[i]
	if lst[i] < lst[i+1]:
		max = lst[i+1]
		
		
for i in range(len(lst)):
	lst[i] = lst[i]/max*100

result = 0
for i in range(len(lst)):
	result = result + lst[i]

print(result/len(lst))

# 이 방식으로 풀었더니 값이 50 하나 들어왔을때가 해결이 안된다.



    