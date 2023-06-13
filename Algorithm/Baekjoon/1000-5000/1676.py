def factorial(n):

    if n==0 or n==1:
        return 1
    return n * factorial(n-1)

n = int(input())
count = 0
num = factorial(n)

numbers = list(map(int,str(num)))

r_numbers = numbers[::-1]

for i in range(len(r_numbers)):
    if r_numbers[i] == 0:
        count+=1
    else:
        break

print(count)












