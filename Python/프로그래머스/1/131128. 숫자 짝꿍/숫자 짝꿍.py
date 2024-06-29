def solution(X, Y):
    arr_x = [0] * 10
    arr_y = [0] * 10
    result = ""

    for i in X:
        arr_x[int(i)] += 1

    for i in Y:
        arr_y[int(i)] += 1

    for i in range(9, -1, -1):
        if arr_x[i] != 0 or arr_y[i] != 0:
            for j in range(min(arr_x[i], arr_y[i])):
                result += str(i)

    if result == "":
        result = "-1"
    elif result[0] == "0":
        result = "0"

    return result
