def solution(priorities, location):
    # 인덱스와 값 리스트 생성
    index_li = []
    for i in range(len(priorities)) :
        index_li.append(i)
    value_li = priorities

    i = 0
    # value 내림차순 정렬이 완료될 때까지 지속
    while not (value_li == sorted(value_li, reverse=True)) :
    # 목록 마지막과 최대값을 비교(작으면 맨뒤로 append)
        if value_li[i] < max(value_li) :
            value_li.append(value_li.pop(i))
            index_li.append(index_li.pop(i))
        else :
            i += i
    return print(index_li.index(location) + 1)

priorities1 = [2, 1, 3, 2]
location1 = 2
solution(priorities1, location1)

priorities2 = [1, 1, 9, 1, 1, 1]
location2 = 0
solution(priorities2, location2)