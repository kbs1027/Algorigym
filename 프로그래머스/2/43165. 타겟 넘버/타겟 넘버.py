from collections import *

def solution(numbers, target):
    answers = 0
    dq = deque()
    cur = numbers.pop(0)
    dq.append(-cur)
    dq.append(cur)
    while len(numbers) != 0:
        cur = numbers.pop(0)
        length = len(dq)
        for i in range(length):
            s = dq.popleft()
            dq.append(s + cur)
            dq.append(s - cur)
    c=Counter(dq)
    return c[target]
            
    