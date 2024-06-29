def solution(phone_number):
    return f'{phone_number[-4:]:*>{len(phone_number)}}'