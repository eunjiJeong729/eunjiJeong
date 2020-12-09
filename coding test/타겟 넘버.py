'''
문제 설명
n개의 음이 아닌 정수가 있습니다. 이 수를 적절히 더하거나 빼서 타겟 넘버를 만들려고 합니다.
예를 들어 [1, 1, 1, 1, 1]로 숫자 3을 만들려면 다음 다섯 방법을 쓸 수 있습니다.

사용할 수 있는 숫자가 담긴 배열 numbers, 타겟 넘버 target이 매개변수로 주어질 때
숫자를 적절히 더하고 빼서 타겟 넘버를 만드는 방법의 수를 return 하도록 solution 함수를 작성해주세요.

참조 링크 : https://programmers.co.kr/learn/courses/30/lessons/43165
'''

# DFS 적용을 위한 경우의 수 생성
def solution(numbers, target):
    answer = 0
    for idx, arg in enumerate(numbers):
        if idx % 2 != 0 :
            numbers[idx] = arg * -1
    return answer

if __name__ == '__main__':
    numbers = [1,1,1,1,1]
    target = 3
    print(solution(numbers,target))
