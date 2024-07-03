function solution(a, b) {
    if (a > b) {
        let tmp = a
        a = b
        b = tmp
    }
    let result = 0
    for (let num = a; num <= b; num++) {
        result += num
    }
    return result
}
