'''
문제 설명
일반적인 프린터는 인쇄 요청이 들어온 순서대로 인쇄합니다. 그렇기 때문에 중요한 문서가 나중에 인쇄될 수 있습니다.
이런 문제를 보완하기 위해 중요도가 높은 문서를 먼저 인쇄하는 프린터를 개발했습니다.
이 새롭게 개발한 프린터는 아래와 같은 방식으로 인쇄 작업을 수행합니다.

현재 대기목록에 있는 문서의 중요도가 순서대로 담긴 배열 priorities와 내가 인쇄를 요청한 문서가 현재 대기목록의 어떤 위치에 있는지를
알려주는 location이 매개변수로 주어질 때, 내가 인쇄를 요청한 문서가 몇 번째로 인쇄되는지 return 하도록 solution 함수를 작성해주세요.

참조 링크 : https://programmers.co.kr/learn/courses/30/lessons/42587
'''
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
    return index_li.index(location) + 1