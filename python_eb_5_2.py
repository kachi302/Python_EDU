# queue sample
from collections import deque
# quoue 구현을 위해서 deque 라이브러리 사용
queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
print(queue)
queue.popleft()
print(queue)
queue.append(1)
queue.append(4)
print(queue)
queue.popleft()
print(queue)
