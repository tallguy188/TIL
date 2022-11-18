'''
최빈값은 주어진 값 중에서 가장 자주 나오는 값을 의미한다. 정수 배열 array가
매개변수로 주어질 때, 최빈값을 return 하도록 solution 함수를 완성해보시오.
최빈값이 여러개면 -1을 return한다.
'''
'''
from collections import Counter

def solution(array):

    cnt = Counter(array)
    mode=  cnt.most_common(2)

    if len(array) == 1:
        return array[0]
    
    if mode[0][1] == mode [1][1] :
        return -1
    else :
        return mode[0][0]

'''

from collections import Counter
def solution(array):
    c = Counter(array)
    order = c.most_common()
    maximum = order[0][1]
    modes = []
    for num in order:
        if num[1] == maximum:
            modes.append(num[0])
    if len(modes)>=2:
        return -1
    else:
        return modes[0]
