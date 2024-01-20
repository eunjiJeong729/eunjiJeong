'''
문제 설명
수포자는 수학을 포기한 사람의 준말입니다. 수포자 삼인방은 모의고사에 수학 문제를 전부 찍으려 합니다. 수포자는 1번 문제부터 마지막 문제까지 다음과 같이 찍습니다.

1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...

1번 문제부터 마지막 문제까지의 정답이 순서대로 들은 배열 answers가 주어졌을 때, 가장 많은 문제를 맞힌 사람이 누구인지 배열에 담아 return 하도록 solution 함수를 작성해주세요.

참조링크 : https://programmers.co.kr/learn/courses/30/lessons/42840
'''

def solution(answers):
    answer = []
    a = len(answers)
    answer1 = [1,2,3,4,5]
    answer1 = answer1 * 10000
    answer1 = answer1[:a]
    answer2 = [2,1,2,3,2,4,2,5]
    answer2 = answer2 * 10000
    answer2 = answer2[:a]
    answer3 = [3,3,1,1,2,2,4,4,5,5]
    answer3 = answer3 * 10000
    answer3 = answer3[:a]

    cnt1 = 0
    cnt2 = 0
    cnt3 = 0
    for i in range(len(answers)) :
        if answer1[i] - answers[i] == 0:
            cnt1 += 1
        if answer2[i] - answers[i] == 0:
            cnt2 += 1
        if answer3[i] - answers[i] == 0:
            cnt3 += 1
    temp = [cnt1, cnt2, cnt3]
    max_temp = max(temp)
    for idx, cnt in enumerate(temp):
        if cnt == max_temp:
            answer.append(idx + 1)
    return answer

if __name__ == '__main__':
    answers1 = [1,2,3,4,5]
    print(solution(answers1))

    answers2 = [1,3,2,4,2]
    print(solution(answers2))