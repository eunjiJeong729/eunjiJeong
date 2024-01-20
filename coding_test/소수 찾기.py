'''
문제 설명
한자리 숫자가 적힌 종이 조각이 흩어져있습니다. 흩어진 종이 조각을 붙여 소수를 몇 개 만들 수 있는지 알아내려 합니다.

각 종이 조각에 적힌 숫자가 적힌 문자열 numbers가 주어졌을 때, 종이 조각으로 만들 수 있는 소수가 몇 개인지 return 하도록 solution 함수를 완성해주세요.

참조 링크 : https://programmers.co.kr/learn/courses/30/lessons/42839
'''

import itertools

def solution(numbers):
    answer = 0
    num = []
    for i in numbers :
        num.append(i)

    # 경우의 수 생성 및 앞자리가 0인 경우 제거, 중복 제거
    num_re = num
    for nums in itertools.permutations(num):
        a = ''.join(nums)
        if a[0] == '0' :
            a = a[1:]
        num_re.append(a)
    num_re = set(num_re)

    # 소수 판별
    temp = []
    if '0' in num_re : num_re.remove('0')
    for x in num_re :
        a = int(x)
        if a != 1 :
            for i in range(2, a):
                if a % i == 0 :
                    b = 0
                    break
                else :
                    b = 1
        else : b = 0
        if b == 1 : temp.append(a)
    answer = len(temp)
    return answer

if __name__ == '__main__':
    numbers1 = "17"
    print(solution(numbers1))
    numbers2 = "011"
    print(solution(numbers2))