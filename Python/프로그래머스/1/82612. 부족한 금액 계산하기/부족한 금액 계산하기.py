def solution(price, money, count):
    nPrice = price * sum(range(count + 1))
    return nPrice - money if nPrice > money else 0