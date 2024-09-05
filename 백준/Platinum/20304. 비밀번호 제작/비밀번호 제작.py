from collections import *

def bfs(password, max_num):
    answer = [100 for _ in range(max_num+1)]
    dq = deque()
    for num in password:
        dq.append(num)
        answer[num] = 0
    while len(dq)!= 0:
        cur = dq.popleft()
        
        for i in range(len(bin(max_num)[2:])):
            x = (1 << i) ^ cur
            if x <= max_num and answer[cur] + 1 < answer[x]:
                answer[x] = answer[cur] + 1
                dq.append(x)
    
    return max(answer)

max_num = int(input())
password_num = int(input())
password = list(map(int, input().split()))

print(bfs(password, max_num))
