Q = [0] * 10
front = -1
rear = -1

rear += 1
Q[rear] = 1 # enQueue(1)

rear += 1
Q[rear] = 2

rear += 1
Q[rear] = 3

while front != rear:
    front += 1
    print(Q[front], end = ' ') # print(deQueue())
print()

listQ = []
listQ.append(1)
listQ.append(2)
listQ.append(3)

while listQ:
    print(listQ.pop(0), end = ' ')
print()


from collections import deque

# enqueue -> append <-> append left
q = deque()
q.append(1)
q.append(2)
q.append(3)

# dequeue -> pop left
while q:
    print(q.popleft())
