import sys
input = sys.stdin.readline
print = sys.stdout.write


n = int(input())


dp = [0]*16

dp[0] = 2

for i in range(1,n+1):
    dp[i] = dp[i-1] + (2**(i-1))


result = (dp[n]**2)

print(str(result))

# n =1 9
# n =2 25
# n =3 81