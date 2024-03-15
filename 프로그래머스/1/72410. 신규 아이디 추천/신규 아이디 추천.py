def solution(new_id):
    new_id = new_id.lower()
    tmp = ""

    for n in new_id:
        if n.isalnum() or n == "-" or n == "_" or n == ".":
            tmp += n

    new_id = tmp

    while True:
        tmp = new_id.replace("..", ".")
        if len(tmp) == len(new_id):
            break
        new_id = tmp

    tmp = tmp.lstrip(".")
    tmp = tmp.rstrip(".")

    if len(tmp) == 0:
        tmp = "a"
    elif len(tmp) >= 16:
        tmp = tmp[:15]
        tmp = tmp.rstrip(".")

    while len(tmp) < 3:
        tmp += tmp[len(tmp) - 1]

    return tmp
