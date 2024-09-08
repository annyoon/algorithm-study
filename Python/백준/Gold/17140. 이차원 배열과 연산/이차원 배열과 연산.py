# 답 참고

def transpose(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    transposed_matrix = [[0 for _ in range(rows)] for _ in range(cols)]
    for i in range(rows):
        for j in range(cols):
            transposed_matrix[j][i] = matrix[i][j]

    return transposed_matrix

def rctranspose(array):
    R = len(array)
    C = len(array[0])
    max_len = 0
    for j in range(R):
        di = {}
        for k in array[j]:
            if k != 1000000000:
                if k in di:
                    di[k] += 1
                else:
                    di[k] = 1
        di_list = list(di.items())
        di_list.sort(key=lambda x: (x[1], x[0]))
        array[j] = []
        for x, y in di_list:
            array[j].append(x)
            array[j].append(y)
            if max_len < len(array[j]):
                max_len = len(array[j])
    for k in range(R):
        if max_len > len(array[k]):
            for t in range(max_len - len(array[k])):
                array[k].append(1000000000)

    return array


r, c, kk = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(3)]
R = len(array)
C = len(array[0])

if R >= r and C >= c and array[r - 1][c - 1] == kk:
    print(0)

else:
    for i in range(100):
        R = len(array)
        C = len(array[0])

        if R >= C:

            array=rctranspose(array)
        else:
            array = transpose(array)

            array=rctranspose(array)

            array = transpose(array)

        R = len(array)
        C = len(array[0])

        if R > 100:
            array = array[:100]
        if C > 100:
            array = transpose(array)
            array = array[:100]
            array = transpose(array)
        if R >= r and C >= c:
            if array[r - 1][c - 1] == kk:
                print(i + 1)
                break
        if i == 99:
            print(-1)