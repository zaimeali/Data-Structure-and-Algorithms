from collections import deque

queue = deque()

queue.appendleft('Google')
queue.appendleft('Facebook')
queue.appendleft('Netflix')
queue.appendleft('Amazon')

print(queue)

queue.pop()
print(queue)