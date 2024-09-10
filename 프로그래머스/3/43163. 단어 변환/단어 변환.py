from collections import *

def solution(begin, target, words):
    dt = {}
    if target not in words:
        return 0
    words.append(begin)
    vl = [False for _ in range(len(words))]
    visit = dict(zip(words,vl))
    for i in range(len(words)):
        for j in range(len(words)):
            if diff_count(words[i], words[j])  == 1:
                if words[i] in dt:
                    dt[words[i]].append(words[j])
                else:
                    dt[words[i]] = [words[j]]
    
    return bfs(dt, visit, begin, target)
    
def diff_count(word1, word2):
    count = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            count+=1
    return count

def bfs(dt, visit, begin, target):
    dq = deque()
    answer = 0
    visit[begin] = True
    for i in range(len(dt[begin])):
        dq.append([dt[begin][i], 1])
        visit[dt[begin][i]] = True
    
    while len(dq) != 0:
        cur = dq.popleft()
        if cur[0] == target:
            answer = cur[1]
            break
        for i in range(len(dt[cur[0]])):
            if visit[dt[cur[0]][i]] == False:
                dq.append([dt[cur[0]][i], cur[1] + 1])
                visit[dt[cur[0]][i]] = True
    return answer