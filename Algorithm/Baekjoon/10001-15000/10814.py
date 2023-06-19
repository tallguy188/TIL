import sys

n = int(sys.stdin.readline())
agename = []

for _ in range(n):
    data = sys.stdin.readline().split()
    age = int(data[0])
    name = data[1].rstrip()  # 개행 문자 제거
    agename.append([age, name])

agename.sort(key=lambda x: x[0])

for k in agename:
    sys.stdout.write(str(k[0]) + " " + k[1] + "\n")

