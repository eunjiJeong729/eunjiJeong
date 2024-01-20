'''
문제 설명
수많은 마라톤 선수들이 마라톤에 참여하였습니다.
단 한 명의 선수를 제외하고는 모든 선수가 마라톤을 완주하였습니다.

마라톤에 참여한 선수들의 이름이 담긴 배열 participant와 완주한 선수들의 이름이 담긴 배열 completion이 주어질 때,
완주하지 못한 선수의 이름을 return 하도록 solution 함수를 작성해주세요.

참조 링크 : https://programmers.co.kr/learn/courses/30/lessons/42576
'''

def solution(participant, completion):
    partici_dic = {}
    for i in participant:
        if i in completion:
            partici_dic[i] = i
        else :
            partici_dic['nopartici'] = i
    answer = partici_dic['nopartici']
    return answer

participant1 = ["leo", "kiki", "eden"]
completion1 = ["eden", "kiki"]
print(solution(participant1, completion1))

participant2 = ["marina", "josipa", "nikola", "vinko", "filipa"]
completion2 = ["josipa", "filipa", "marina", "nikola"]
print(solution(participant2, completion2))
