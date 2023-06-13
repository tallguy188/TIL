import sys

input = sys.stdin.readline
n = int(input())  # n을 입력받음

numbers = [int(input()) for _ in range(n)]
numbers.sort()

print = sys.stdout.write
for element in numbers:
    print(str(element) + '\n')







