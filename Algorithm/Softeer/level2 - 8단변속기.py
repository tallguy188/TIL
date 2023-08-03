import sys

num = list(map(int,sys.stdin.readline().split()))


word = ''

for i in range(len(num)-1):
    if num[i+1] == num[i]+1:
        word = 'ascending'
        continue

    elif num[i+1] == num[i] -1:
        word = 'descending'
        continue

    elif num[i+1] != num[i] +1 or num[i+1] != num[i] -1:
        word = 'mixed'
        break

sys.stdout.write(word)


