def solution(cacheSize, cities):
    result = 0
    arr = []
    
    if cacheSize == 0:
        return len(cities) * 5
    
    for city in cities:
        flag = False
        for i in range(len(arr)):
            if arr[i].lower() == city.lower():
                flag = True
                arr.pop(i)
                result += 1
                break
        if not flag:
            if len(arr) == cacheSize:
                arr.pop(0)
            result += 5
        arr.append(city)
        
    return result