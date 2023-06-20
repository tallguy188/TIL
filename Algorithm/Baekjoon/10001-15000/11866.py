from collections import deque

n,k = map(int,input().split())

deq = deque()
for i in range(n):
    deq.append(i+1)

    # [1,2,3,4,5,6,7]

result = []

start = 0
while deq:      # 데크가 비어있지 않은 동안 반복을 실행
    start = (start+k-1) % len(deq)
    removed = deq[start]
    deq.remove(removed)
    result.append(str(removed))


output = "<" + ", ".join(result) + ">"
print(output)















