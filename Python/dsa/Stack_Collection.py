from collections import deque

stack = deque()

stack.append('Google')
stack.append('Facebook')
stack.append('Amazon')
stack.append('Netflix')

print(stack)

stack.pop()

print(stack)