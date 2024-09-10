from collections import *

def solution(n, computers):
    return bfs(computers, n)
    
def bfs(computers, n):
    check = [False for _ in range(n)]
    num = 0
    for i in range(len(check)):
        dq = deque()
        
        if check[i] == False:
            num +=1
            print(i)
            for j in range(len(check)):  
                if check[j] == False and computers[i][j] == 1:
                    dq.append(j)
                    print(f"append: {j}")
                    check[j] = True
                    
            while len(dq) != 0:
                cur = dq.popleft()
                for j in range(len(check)):  
                    if check[j] == False and computers[cur][j] == 1:
                        dq.append(j)
                        check[j] = True
    return num
                
    