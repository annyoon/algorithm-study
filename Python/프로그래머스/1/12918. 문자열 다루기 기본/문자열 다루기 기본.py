def solution(string):
    if len(string) != 4 and len(string) != 6:
        return False
    for s in string:
        if ord('0') > ord(s) or ord('9') < ord(s):
            return False
    return True