def find_most_common_letter(word):

    word = word.lower()
    # 알파벳의 등장 횟수를 저장할 딕셔너리를 생성
    letter_counts = {}

    for letter in word:
        # 알파벳이 이미 딕셔너리에 등록되어 있는 경우 등장 횟수를 1 증가
        if letter.isalpha():   # 입력받은 단어가 알파벳이면
            if letter in letter_counts:
                letter_counts[letter] += 1
            else:
                letter_counts[letter] = 1

    # 가장 많이 사용된 알파벳들을 찾음
    max_count = max(letter_counts.values())
    # 리스트 컴프리핸션으로 가장 많이 나온 단어를 리스트에 저장
    most_common_letters = [letter.upper() for letter, count in letter_counts.items() if count == max_count]

    # 가장 많이 사용된 알파벳이 여러 개인 경우 "?"를 출력
    if len(most_common_letters) > 1:
        return "?"
    else:
        return most_common_letters[0]
# 사용자로부터 알파벳으로 된 단어를 입력
word = input()

most_common = find_most_common_letter(word)

print( most_common)




