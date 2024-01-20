'''
문제 설명
Leo는 카펫을 사러 갔다가 아래 그림과 같이 중앙에는 노란색으로 칠해져 있고 테두리 1줄은 갈색으로 칠해져 있는 격자 모양 카펫을 봤습니다.

Leo는 집으로 돌아와서 아까 본 카펫의 노란색과 갈색으로 색칠된 격자의 개수는 기억했지만, 전체 카펫의 크기는 기억하지 못했습니다.

Leo가 본 카펫에서 갈색 격자의 수 brown, 노란색 격자의 수 yellow가 매개변수로 주어질 때
카펫의 가로, 세로 크기를 순서대로 배열에 담아 return 하도록 solution 함수를 작성해주세요.

참조 링크 : https://programmers.co.kr/learn/courses/30/lessons/42842
'''

def solution(brown, yellow):
    answer = []
    # yellow 약수 구하기
    yellow_wh_li = []
    for i in range(1, yellow + 1):
        if yellow % i == 0:
            h = yellow//i
            if i >= h :
                yellow_wh = i, h
                yellow_wh_li.append(yellow_wh)

    for j in yellow_wh_li :
        if brown == (j[0] + 2) * (j[1] + 2) - yellow:
            answer.append(j[0] + 2)
            answer.append(j[1] + 2)

    return answer

if __name__ == '__main__':
    brown1 = 10
    yellow1 = 2
    print(solution(brown1, yellow1))

    brown2 = 8
    yellow2 = 1
    print(solution(brown2, yellow2))

    brown3 = 24
    yellow3 = 24
    print(solution(brown3, yellow3))