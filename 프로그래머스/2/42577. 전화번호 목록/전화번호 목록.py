import collections

def solution(phone_book):
    pb = sorted(set(phone_book))
    for i in range(1, len(pb)):
        if pb[i].startswith(pb[i-1]):
            return False
    return True