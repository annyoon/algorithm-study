def solution(numbers):
    answer = []
    
    for number in numbers:
        flag = False
        number = list(bin(number)[2:])
        for i in range(len(number) - 1, -1, -1):
            if number[i] == '0':
                number[i] = '1'
                if i < len(number) - 1:
                    number[i + 1] = '0'
                flag = True
                break
        if not flag:
            number[0] = '0'
            number = ['1'] + number
        answer.append(int(''.join(number), 2))
        
    return answer
