from collections import *

def solution(participant, completion):
    p = Counter(participant)
    c = Counter(completion)
    answer = p - c
    return list(answer.keys())[0]