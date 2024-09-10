from collections import *

def solution(maps):
    return bfs(maps)
def bfs(maps):
    check = []
    cl = len(maps)
    rl = len(maps[0])
    for i in range(cl):
        a = []
        for j in range(rl):
            a.append(False)
        check.append(a)

    c = [1,0,0,-1]
    r = [0,1,-1,0]
    
    dq = deque()
    answer = -1
    dq.append([[0,0], 1])
    check[0][0] = True
    while len(dq) != 0:
        cur = dq.popleft()
        for i in range(4):
            if  0 <= cur[0][0] + c[i]  < cl and 0 <= cur[0][1] + r[i] < rl:
                if cur[0][0] + c[i] == cl - 1 and cur[0][1] + r[i] == rl - 1:
                    answer = cur[1] + 1
                    return answer
                if maps[cur[0][0] + c[i]][cur[0][1] + r[i]] == 1:
                    if check[cur[0][0] + c[i]][cur[0][1] + r[i]] == False:
                        dq.append([[cur[0][0] + c[i], cur[0][1] + r[i]], cur[1] + 1])
                        check[cur[0][0] + c[i]][cur[0][1] + r[i]] = True
    return answer

    