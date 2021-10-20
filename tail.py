from collections import deque

def tail(f, num):
    dq = deque([], maxlen=num)
    for line in f:
        dq.append(line)
    for line in dq:
        print(dq)

f = open('poem.txt')
tail(f, 3)
f.close()