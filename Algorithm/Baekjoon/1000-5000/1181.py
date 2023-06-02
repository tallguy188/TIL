def arrange_word(words):

    result = []
    for word in words:
        if word not in result:
            result.append(word)

    return sorted(result, key=lambda x: (len(x), x))


n = int(input())
s_list = [input() for _ in range(n)]

sorted_list = arrange_word(s_list)
for i in range(len(sorted_list)):
    print(sorted_list[i], sep='\n')




