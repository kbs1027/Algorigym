from collections import *
from math import *
import heapq
import sys


def solution(priorities, location):
    mapped_p = map_p(priorities)
    set_sorted_p = set_sort_p(priorities)
    print(set_sorted_p)
    return check(mapped_p, set_sorted_p, location)

def map_p(priorities):
    p = []
    for i in range(len(priorities)):
        p.append([priorities[i],i])
    return p

def set_sort_p(priorities):
    s = Counter(priorities)
    s = sorted(s.items(), key=lambda x : x[0] ,reverse = True)
    return s

def check(mp, ssp, loc):
    dq = deque()
    p_ssp = list(dict(ssp).keys())
    c_ssp = list(dict(ssp).values())
    for i in range(len(mp)):
        dq.append(mp[i])
    
    num =0
    c = 0
    print(p_ssp, c_ssp)
    for i in range(len(p_ssp)):
        c_count = 0
        while c_count < c_ssp[i]:
            print(c_count, c_ssp[i])
            cur = dq.popleft()
            if cur[0] == p_ssp[i]:
                num += 1
                c_count += 1
                if cur[1] == loc:
                    return num
            else:
                dq.append(cur)  
    return 0
            