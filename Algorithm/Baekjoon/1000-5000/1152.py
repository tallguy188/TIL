def count_words(text):
    # 문자열을 소문자로 변환하여 모든 단어를 정확히 비교하기 위해 통일
    text = text.lower()

    # 문자열을 공백을 기준으로 단어들로 분리
    words = text.split()

    # 단어갯수 저장변수 생성
    count = 0

    # 단어들을 하나씩 순회하며 갯수 저장
    for word in words:
        count +=1
    return count



text = input()


word_count = count_words(text)


print(word_count)

