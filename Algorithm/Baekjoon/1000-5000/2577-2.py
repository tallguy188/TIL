"""
세 개의 자연수 A, B, C가 주어질 때 A × B × C를 계산한 결과에 0부터 9까지 각각의 숫자가 몇 번씩 쓰였는지를 구하는 프로그램을 작성하시오.
예를 들어 A = 150, B = 266, C = 427 이라면 A × B × C = 150 × 266 × 427 = 17037300 이 되고, 계산한 결과 17037300 에는 0이 3번, 1이 1번, 3이 2번, 7이 2번 쓰였다.

"""

a,b,c = [int(input()) for _ in range(3)]  # 한번에 입력하는 방법
 
r = list(str(a*b*c))   # 리스트에 저장될 때 ("17304314") 이런식으로 저장되는게 아니라 ("1","7",...)이런식으로 저장됨 

for i in range(10):
	print(r.count(str(i)))