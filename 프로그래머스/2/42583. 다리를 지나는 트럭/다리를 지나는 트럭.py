from collections import deque

def solution(bridge_length, weight, truck_weights):
    # 다리 길이가 1일 경우
    if bridge_length == 1:
        answer = len(truck_weights) + 1
        return answer
    
    # 트럭이 1대일 경우
    if len(truck_weights) == 1:
        answer = weight + 1
        return answer
    
    # 그 외 경우
    bridge = deque([0] * (bridge_length - 1))
    bridge.append(truck_weights[0])
    bridge_sum = truck_weights[0]
    time = 1
    
    for i in range(1, len(truck_weights)):
        truck = bridge.popleft()
        bridge_sum -= truck
        time += 1
        
        while bridge_sum + truck_weights[i] > weight:
            bridge.append(0)
            truck = bridge.popleft()
            bridge_sum -= truck
            time += 1
            
        bridge.append(truck_weights[i])
        bridge_sum += truck_weights[i]
        
    answer = time + bridge_length

    return answer