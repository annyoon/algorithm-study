function solution(x) {
    return x % x.toString().split('').reduce((sum, cur) => sum + Number(cur), 0) == 0
}
