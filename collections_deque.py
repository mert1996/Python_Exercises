from collections import deque

lines = int(input())
d = deque()

for i in range(lines):
    inputt = input().split()

    command = inputt[0]

    if command == "append":
        value   = int(inputt[1])
        d.append(value)
    if command == "appendleft":
        value   = int(inputt[1])
        d.appendleft(value)
    if command == "pop":
        d.pop()
    if command == "popleft":
        d.popleft()

print(*d)
