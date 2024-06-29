def solution(s):
    letter = ""
    count1, count2, result = 0, 0, 0

    for cur in s:
        if letter == "":
            letter = cur
        if cur == letter:
            count1 += 1
        else:
            count2 += 1
        if count1 == count2:
            result += 1
            letter = ""

    if letter != "":
        result += 1

    return result
