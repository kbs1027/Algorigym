from collections import *

def solution(arr):
    answer = []
    before = arr[0]
    for i in range(len(arr)):
        if arr[i] != before:
            answer.append(before)
        before = arr[i]
        if i == len(arr) -1 :
            answer.append(arr[i])
    return answer