function solution(n)
{
    let result = 0
    for (let number of n.toString()){
        result += parseInt(number)
    }
    return result
}
