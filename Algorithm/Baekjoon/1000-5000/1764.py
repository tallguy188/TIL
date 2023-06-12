n, m = map(int,input().split())  # n, m값을 입력받음

n_set = set(input() for _ in range(n))

m_set = set(input() for _ in range(m))

# 집합을 리스트로 변환
nm_set = sorted(list(n_set.intersection(m_set)))

print(len(nm_set))
for name in nm_set:
    print(name)

"""
이 문제는 시간복잡도를 고려해서 풀어야 하는 문제이다.
처음 문제를 읽고 이중반복문을 사용해서 문제를 풀려고 시도했다. 하지만 주어진 조건에 따라 n과 m값이 
500000까지 커지면 자연스럽게 시간복잡도가 증가할 수밖에 없다. 따라서 집합자료형으로 간단하게 푸는 방법이 
문제의 해결법이다. 
"""





