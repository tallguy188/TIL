from collections import deque

# Contain 1, 2, 3, 4, 5 in deq
deq = deque([1, 2, 3, 4, 5])

deq.rotate(1)
print(deq)
# deque([5, 1, 2, 3, 4])

deq.rotate(-1)
print(deq)
# deque([1, 2, 3, 4, 5])

