from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge = deque([0] * bridge_length, maxlen = bridge_length)
    answer, cur, i = 0, 0, 0
    
    while i < len(truck_weights):
        if cur + truck_weights[i] - bridge[0] <= weight:
            cur += (truck_weights[i] - bridge[0])
            bridge.append(truck_weights[i])
            i += 1
        else:
            cur -= bridge[0]
            bridge.append(0)
        answer += 1
        
    return answer + bridge_length
