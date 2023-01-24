# 폴리오미노

'''
민식이는 다음과 같은 폴리오미노 2개를 무한개만큼 가지고 있다. AAAA와 BB

이제 '.'와 'X'로 이루어진 보드판이 주어졌을 때, 민식이는 겹침없이 'X'를 모두 폴리오미노로 덮으려고 한다. 이때, '.'는 폴리오미노로 덮으면 안 된다.

폴리오미노로 모두 덮은 보드판을 출력하는 프로그램을 작성하시오.

입력: 첫째 줄에 보드판이 주어진다. 보드판의 크기는 최대 50이다.

출력: 첫째 줄에 사전순으로 가장 앞서는 답을 출력한다. 만약 덮을 수 없으면 -1을 출력한다.

'''

'''
a = input()

num = a.count('X')

split_a = a.split('.')

#print(split_a)

result = -1

# for문 안에 넣어줘야됨


for i in range(len(split_a)):
    if num % 2 != 0:
        print(result)
        break
    
    b = len(split_a[i])


    print(b)
'''

n = input()
N = list()
for i in range(len(n)) : #문자열을 리스트로 바꾸기
    N.append(n[i]) 
c = 0 #개수를 세는 변수
E = 0 #문제가 생기면 1, 아니면 0
r = N 
for i in range(len(N)) :
    c += 1 #개수 세기
    if (N[i] == ".") | (i == (len(N)-1)): #.이거나 문자열의 끝
        if (N[i] == ".") :
            c -= 1 #.까지 셌으니까 하나 빼주기
        if c % 2 != 1 :
            A = i-c #수정할 부분의 시작
            B = i   #끝
            if (i == (len(N)-1)) :
                A = i-c+1 #문자열의 끝까지 오면 하나씩 더해줌
                B = i+1 #얘도 똑같이 더해줌
            while(True) :
                if (A + 4) <= B : #4개 이상 바꿀 수 있으면 
                    r[A:A+4] = "AAAA"
                    A += 4
                elif (A + 2) <= B : #2개만 되면
                    r[A:A+2] = "BB"
                    A += 2
                else : # A == B
                    break
        else : # 개수가 홀수면
            E = 1
        c = 0
if E : 
    print(-1)
else :
    R = ''
    for i in r :
        R += i
    print(R)

