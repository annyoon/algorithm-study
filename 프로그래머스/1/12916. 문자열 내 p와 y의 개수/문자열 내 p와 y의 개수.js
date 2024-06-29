function solution(s){
    pNum = s.split('p').length + s.split('P').length - 2
    yNum = s.split('y').length + s.split('Y').length - 2
    
    if (pNum == yNum){
        return true
    }
    return false
}
