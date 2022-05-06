"""
파이썬 사칙연산 7가지 연산자
+: 덧셈
-: 뺄셈
*: 곱하기
**: 거듭 제곱
/ : 나누기
// : 나누기 연산 후 소수점 이하의 수를 버리고, 정수 부분의 수만 구하기
% : 나누기 연산 후 몫이 아닌 나머지를 구함 
"""






count = 0
old =  int(input())
N = old

while True:
	result = (N // 10) + (N % 10)
	N = (N % 10) * 10 + (result % 10)
	count = count +1
		
	if(N == old):
		break
		
print(count)
