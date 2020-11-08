def solution(bridge_length, weight, truck_weights):
    # 다리 길이만큼 빈 리스트 생성
    bridge = [0] * bridge_length

    # 다리의 최대 수용 무게
    bridge_weight = weight

    # 다리에 트럭 올리기
    temp = []
    time = 0
    while bridge != temp:
        bridge.pop(0)
        time += 1
        if truck_weights != temp :
            if sum(bridge) + truck_weights[0] < bridge_weight :
                bridge.append(truck_weights.pop(0))
            else :
                bridge.append(0)
    answer = time
    return answer


bridge_length1 = 2
weights1 = 10
truck_weights1 = [7,4,5,6]
print(solution(bridge_length1, weights1, truck_weights1))

bridge_length2 = 100
weights2 = 100
truck_weights2 = [10]
print(solution(bridge_length2, weights2, truck_weights2))

bridge_length3 = 100
weights3 = 100
truck_weights3 = [10,10,10,10,10,10,10,10,10,10]
print(solution(bridge_length3, weights3, truck_weights3))