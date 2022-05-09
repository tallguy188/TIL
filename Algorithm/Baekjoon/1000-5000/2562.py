"""
9개의 서로 다른 자연수가 주어질 떄, 이들 중 최댓값을 찾고 그 최댓값이 몇번째 수인지 구하는 프로그램을 작성하시오. 
"""

i = 1
a = []
while i<=9 : 
	N = int(input())
	a.append(N)
	if (len(a)==9):
		break

print(max(a))
print(a.index(max(a))+1)



# break문을 만들어주지 않으면 제대로 출력이 되지 않는다. 
