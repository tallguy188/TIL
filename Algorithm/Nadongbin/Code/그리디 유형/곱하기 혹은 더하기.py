s = input('숫자를 입력하시오:')
# s라는 변수에 문자열이 입력된다.


result = int(s[0])

for i in range(1,len(s)):

    num = int (s[i])

    if num <=1 or result <=1:
        result += num
    else:
        result *= num

print(result)
    
        

    

    
