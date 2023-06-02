def fellindrom(words):

    rlist = []

    # 각 입력받은 리스트 숫자마다 거꾸로 뒤집어도 똑같나 확인
    for word in words:
        r_word = word[::-1]
        if r_word == word:
            rlist.append('yes')
        else:
            rlist.append('no')

    return rlist

word_list = []
while True:
    word = input()
    if word == '0':
        break
    word_list.append(word)


result = fellindrom(word_list)

for str in result:
    print(str, sep='\n')


















