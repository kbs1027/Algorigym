from collections import *
from math import *

def solution(progresses, speeds):
    answer = []
    dq = deque()
    for i in range(len(speeds)):
        need = ceil((100 - progresses[i])/speeds[i])
        dq.append(need)
    
    f = 0
    
    while len(dq) != 0 :
        cur = dq.popleft()
        num = 0
        for i in range(len(dq)):
            if dq[i] <= cur:
                num += 1
            else:
                break
        for j in range(num):
            dq.popleft()
        answer.append(num+1)
    
    return answer
    
        
        