# n = int(input())
#
# nums = set(map(int,input().split()))
#
# m = int(input())
#
# mums = set(map(int,input().split()))
#
# result =[]
#
# for mum in mums:
#
#     if mum in nums:
#
#         result.append(1)
#     else:
#
#         result.append(0)
#
# for k in result:
#     print(k)
import sys

n = int(sys.stdin.readline())
nums = set(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
mums = list(map(int, sys.stdin.readline().split()))
result = []
for mum in mums:
    if mum in nums:
        result.append(1)
    else:
        result.append(0)

for k in result:
     print(k)