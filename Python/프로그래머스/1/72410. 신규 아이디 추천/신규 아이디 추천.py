def solution(new_id):
    answer = ""

    for i in new_id.lower():
        if i.isalnum() or i == "-" or i == "_" or i == ".":
            if len(answer) == 0 or not (answer[len(answer) - 1] == "." and i == "."):
                answer += i

    answer = answer.strip(".")

    if len(answer) == 0:
        answer = "a"
    elif len(answer) >= 16:
        answer = answer[:15].strip(".")

    while len(answer) <= 2:
        answer += answer[len(answer) - 1]

    return answer
