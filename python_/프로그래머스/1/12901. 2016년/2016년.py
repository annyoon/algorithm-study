def solution(a, b):
    days = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    month_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    num = 0
    
    for i in range(a - 1):
        num += month_days[i]
        
    num += b - 1
    
    return days[num % 7]