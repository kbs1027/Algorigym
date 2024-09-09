from collections import *

def solution(clothes):
    lt = []
    for i in range(len(clothes)):
        lt.append(clothes[i][1])
    c = list(Counter(lt).values())
    answer = 1
    for i in range(len(c)):
        answer *= (c[i]+1)
    return answer - 1