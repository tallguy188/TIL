# 폴리오미노

'''
민식이는 다음과 같은 폴리오미노 2개를 무한개만큼 가지고 있다. AAAA와 BB

이제 '.'와 'X'로 이루어진 보드판이 주어졌을 때, 민식이는 겹침없이 'X'를 모두 폴리오미노로 덮으려고 한다. 이때, '.'는 폴리오미노로 덮으면 안 된다.

폴리오미노로 모두 덮은 보드판을 출력하는 프로그램을 작성하시오.

입력: 첫째 줄에 보드판이 주어진다. 보드판의 크기는 최대 50이다.

출력: 첫째 줄에 사전순으로 가장 앞서는 답을 출력한다. 만약 덮을 수 없으면 -1을 출력한다.

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

    '''
    if len(split_a[i]) == 2:
        split_a[i] = 'BB'
    '''

    print(b)
    

    

