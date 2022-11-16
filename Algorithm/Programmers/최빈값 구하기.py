'''
최빈값은 주어진 값 중에서 가장 자주 나오는 값을 의미한다. 정수 배열 array가
매개변수로 주어질 때, 최빈값을 return 하도록 solution 함수를 완성해보시오.
최빈값이 여러개면 -1을 return한다.
'''

def solution(array):
keys = set(array)
dict = {}
max_freq = []
for key in keys:
dict[key] = array.count(key)
for key in keys:
if dict[key] == max(dict.values()):
max_freq.append(key)
if len(max_freq) > 1:
answer = -1
else:
answer = max_freq[0]
return answer

#풀어가는중..
