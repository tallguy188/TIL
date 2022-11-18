'''
첫번쨰 분수의 분자와 분모를 뜻하는 denum1,num1,두번째 분수의 분자와 분모를
뜻하는 denum2, num2가 매개변수로 주어진다. 두 분수를 더한 값을 기약 분수로
나타내었을 때, 분자와 분모를 순서대로 담은 배열을 return 하는 solution 함수를
완성하시오

'''
# 기약분수 = 분모와 분자를 최대공약수로 나눌것
import math
def solution(denum1, num1, denum2, num2):
    answer = []
    
    if (num1 % num2 == 0 or num2 % num1 == 0) :
        num = num1 * num2
        denum = denum1 * num2  + denum2 * num1
        great = math.gcd(num,denum)
        answer = [denum/great,num/great]
    else:
        num = num1*num2
        denum = denum1*num2 + denum2*num1
        great = math.gcd(num,denum)
            
        answer = [denum/great,num/great]
    return answer
  
