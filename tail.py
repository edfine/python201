from collections import deque

def tail(f, num):
    dq = deque([], maxlen=num)
    for line in f:
        dq.append(line)
    for line in dq:
        print(dq)
        # return dq

if __name__=='__main__':
    with open('poem.txt') as f:
        tail(f, 3)
        f.close()