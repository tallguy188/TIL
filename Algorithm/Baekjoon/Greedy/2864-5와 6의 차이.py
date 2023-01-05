# 5와 6의 차이
'''
상근이는 2863번에서 표를 너무 열심히 돌린 나머지 5와 6을 헷갈리기 시작했다.

상근이가 숫자 5를 볼 때, 5로 볼 때도 있지만, 6으로 잘못 볼 수도 있고, 6을 볼 때는, 6으로 볼 때도 있지만, 5로 잘못 볼 수도 있다.

두 수 A와 B가 주어졌을 때, 상근이는 이 두 수를 더하려고 한다. 이때, 상근이가 구할 수 있는 두 수의 가능한 합 중, 최솟값과 최댓값을 구해 출력하는 프로그램을 작성하시오.

입력:첫째 줄에 두 정수 A와 B가 주어진다.

출력:첫째 줄에 상근이가 구할 수 있는 두 수의 합 중 최솟값과 최댓값을 출력한다.

'''

a,b  = input().split()

c = a

d = b

new_a = a.replace('6','5')
new_a = int(new_a)


new_b = b.replace('6','5')
new_b = int(new_b)


new_c = c.replace('5','6')
new_c= int(new_c)

new_d = d.replace('5','6')
new_d = int(new_d)

#print(new_a,new_b,new_c,new_d)


e = new_a + new_b
f = new_c + new_d

print(e,f)


    

