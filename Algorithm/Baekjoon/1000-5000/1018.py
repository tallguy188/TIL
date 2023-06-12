def count_board(board,ideal_board):
    """
    시작하는 타일 색을 바탕으로 idealboard를 넣어줘서 기존 board와 비교 후 바꿀 타일의 개수를 세어줌.
    """
    count = 0
    for i in range(8):
        for j in range(8):
            if board[i][j] != ideal_board[i][j]:
                count +=1

    return count




N, M = map(int, input().split())

board = [list(map(str, input())) for _ in range(N)]

idealBoardB = [['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], \
              ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], \
              ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], \
              ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], \
              ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], \
              ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], \
              ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], \
              ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']]

idealBoardA = [['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], \
               ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], \
               ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], \
               ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], \
               ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], \
               ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], \
               ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], \
               ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], \
               ]

# 8*8 타일을 선택해주는 로직

min_count = float('inf')

for i in range(N-7):
    for j in range(M-7):
        sub_board = [row[j:j+8] for row in board[i:i+8]]
        count1 = count_board(sub_board, idealBoardB)
        count2 = count_board(sub_board, idealBoardA)
        min_count = min(min_count, count1, count2)

print(min_count)
