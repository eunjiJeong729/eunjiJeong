'''
문제설명
전화번호부에 적힌 전화번호 중,
한 번호가 다른 번호의 접두어인 경우가 있는지 확인하려 합니다.
전화번호가 다음과 같을 경우, 구조대 전화번호는 영석이의 전화번호의 접두사입니다.

구조대 : 119
박준영 : 97 674 223
지영석 : 11 9552 4421
전화번호부에 적힌 전화번호를 담은 배열 phone_book 이 solution 함수의 매개변수로 주어질 때,
어떤 번호가 다른 번호의 접두어인 경우가 있으면 false를 그렇지 않으면 true를 return 하도록 solution 함수를 작성해주세요.

참조 : https://programmers.co.kr/learn/courses/30/lessons/42577
'''

def solution(phone_book):
    answer = True
    phone_book.sort()
    for i,j in zip(phone_book, phone_book[1:]):
        if j.startswith(i):
            answer = False
    return answer

phone_book1 = ["119", "97674223", "1195524421"]
print(solution(phone_book1))

phone_book2 = ["123","456","789"]
print(solution(phone_book2))

phone_book3 = ["12","123","1235","567","88"]
print(solution(phone_book3))