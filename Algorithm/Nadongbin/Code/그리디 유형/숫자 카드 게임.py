# 숫자 카드 게임


# N과 M 입력받기

n,m = map(int,input().split())

result  = 0
mylist  = []
for i in range(n):
    mylist= list(map(int,input().split()))
    min_value = 10001  # 최솟값으로 임의의 큰수를 지정 
    for a in mylist:
        if a < min_value:
            min_value = a
    result = max(result,min_value)

print(result)
    
    
