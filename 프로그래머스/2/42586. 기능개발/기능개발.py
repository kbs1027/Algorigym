from collections import *
from math import *

def solution(progresses, speeds):
    ps = list(zip(progresses, speeds))
    dq = deque(ps)
    num =0
    answer = []
    while len(dq) != 0:
        num += 1
        co = 0
        while dq[0][0] + dq[0][1] * num >= 100:
            dq.popleft()
            co += 1
            if len(dq) == 0 :
                break
        if co != 0:
            answer.append(co)
    return answer