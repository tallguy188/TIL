import sys

print = sys.stdout.write

# 바이러스의 수 k , 증가율 p , 총시간 N초
k, p, n = map(int, sys.stdin.readline().split())

result = (k * pow(p, n, 1000000007)) % 1000000007
print(str(result))