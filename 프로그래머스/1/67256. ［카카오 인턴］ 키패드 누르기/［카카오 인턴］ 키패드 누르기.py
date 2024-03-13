def solution(numbers, hand):
    dist = {0:0, 1:1, 2:2, 3:1, 4:2, 5:3, 6:2, 7:3, 8:4, 9:3, 10:4}
    cur_l = 10
    cur_r = 12
    result = ''
    
    for n in numbers:
        if n == 1 or n == 4 or n == 7:
            result += 'L'
            cur_l = n
        elif n == 3 or n == 6 or n == 9:
            result += 'R'
            cur_r = n
        else:
            if n == 0:
                n = 11
            dist_l = dist[abs(n - cur_l)]
            dist_r = dist[abs(n - cur_r)]
            
            if dist_r < dist_l:
                result += 'R'
                cur_r = n
            elif dist_r > dist_l:
                result += 'L'
                cur_l = n
            else:
                if hand == 'right':
                    result += 'R'
                    cur_r = n
                elif hand == 'left':
                    result += 'L'
                    cur_l = n
                    
    return result