def solution(storey):
    length = len(str(storey)) - 1

    if length == 0:
        return min(storey, 11 - storey)

    sub = 10 ** (length + 1) - storey
    
    result1 = storey // (10 ** length) + solution(storey % (10 ** length))
    result2 = 1 + sub // (10 ** length) + solution(sub % (10 ** length))

    return min(result1, result2)
