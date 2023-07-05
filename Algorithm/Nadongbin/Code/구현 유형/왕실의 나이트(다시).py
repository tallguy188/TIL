
a = input()

row = int(a[1])

column = int(ord(a[0])) - ord('a') + 1

nexts = [(-2,1),(-2,-1),(2,1),(2,-1),(1,-2),(1,2),(-1,-2),(-1,2)]

result = 0
for next in nexts:
    next_row = row + next[0]
    next_column = column + next[1]

    if next_row > 0 and next_row < 9  and next_column >0 and next_column <9:
        result +=1


print(result)