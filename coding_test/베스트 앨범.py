'''
문제설명
스트리밍 사이트에서 장르 별로 가장 많이 재생된 노래를 두 개씩 모아 베스트 앨범을 출시하려 합니다.
노래는 고유 번호로 구분하며, 노래를 수록하는 기준은 다음과 같습니다.

속한 노래가 많이 재생된 장르를 먼저 수록합니다.
장르 내에서 많이 재생된 노래를 먼저 수록합니다.
장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록합니다.
노래의 장르를 나타내는 문자열 배열 genres와 노래별 재생 횟수를 나타내는 정수 배열 plays가 주어질 때,
베스트 앨범에 들어갈 노래의 고유 번호를 순서대로 return 하도록 solution 함수를 완성하세요.

참조 링크 : https://programmers.co.kr/learn/courses/30/lessons/42579
'''

def solution(genres, plays):
    answer = []
    dic_num = {}
    classic_cnt = 0
    pop_cnt = 0
    classic_cnt_list = []
    pop_cnt_list = []
    for i in plays:
        dic_num[i] = plays.index(i)
    for i, j in zip(genres,plays):
        if i == 'classic':
            classic_cnt += j
            classic_cnt_list.append(j)
        else :
            pop_cnt += j
            pop_cnt_list.append(j)

    if classic_cnt > pop_cnt :
        pop_cnt_list.sort(reverse=True)
        classic_cnt_list.sort(reverse=True)
        addlist = classic_cnt_list[:2] + pop_cnt_list[:2]
        for i in addlist:
            answer.append(dic_num[i])
    else:
        pop_cnt_list.sort(reverse=True)
        classic_cnt_list.sort(reverse=True)
        addlist = pop_cnt_list[:2] + classic_cnt_list[:2]
        for i in addlist:
            answer.append(dic_num[i])
    return answer

genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]
print(solution(genres, plays))