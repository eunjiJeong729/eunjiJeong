import requests
from bs4 import BeautifulSoup
import re

# mod1.py는 클래스에서 멤버 변수가 동작할 기능을 구현한 곳임. 클래스에서 멤버함수를 생성할 때 import하여 사용할 예정임

def getel(pagenumber):
    # 레시피 사이트에서 요리 재료와 필요수량을 크롤링하여 저장함
    url_start = 'http://www.10000recipe.com/recipe/'
    url = url_start + str(pagenumber)
    # pagenumber를 매개변수로 레시피마다 생성된 객체에 저장시킴
    result = requests.get(url)
    soup = BeautifulSoup(result.text, "html.parser")
    score_result = soup.find('div', class_='ready_ingre3')
    review = {}
    for lili in score_result.find_all('ul'):
        for li in score_result.find_all('li'):
            pattern = '\S*'
            # 크롤링할 데이터의 형식이 공백과 불필요한 내용이 포함되어 정규표현식을 활용함
            p = re.compile(pattern)
            m = p.match(li.text)
            reviews = {m.group(): li.find('span', class_='ingre_unit').text}
            # 필요한 데이터 재료이름과 필요수량을 딕셔너리로 저장함
            review.update(reviews)
    return review

def getrecipe_name(pagenumber):
    # 레시피 사이트에서 요리 이름을 크롤링하여 저장하는 함수임
    url_start = 'http://www.10000recipe.com/recipe/'
    url = url_start + str(pagenumber)
    result = requests.get(url)
    soup = BeautifulSoup(result.text, "html.parser")
    score_result = soup.find('div', class_='view2_summary')
    a = score_result.find('h3').text
    return a

def getrecipe_time(pagenumber):
    # 레시피 사이트에서 해당 요리를 요리할 때 걸리는 시간을 크롤링하여 저장하는 함수임.
    url_start = 'http://www.10000recipe.com/recipe/'
    url = url_start + str(pagenumber)
    result = requests.get(url)
    soup = BeautifulSoup(result.text, "html.parser")
    score_result = soup.find('div', class_='view2_summary_info')
    b = score_result.find('span', class_='view2_summary_info2').text
    return b

def getrecipe_level(pagenumber):
    # 레시피 사이트에서 해당 요리의 난이도를 크롤링하여 저장하는 함수임.
    url_start = 'http://www.10000recipe.com/recipe/'
    url = url_start + str(pagenumber)
    result = requests.get(url)
    soup = BeautifulSoup(result.text, "html.parser")
    score_result = soup.find('div', class_='view2_summary_info')
    c = score_result.find('span', class_='view2_summary_info3').text
    return c

def shpwrecipe_descrip(pagenumber):
    # 해당 요리의 상세 레시피 순서를 알려주기 위해 사용자가 원할 경우 레시피 사이트 주소를 리턴해줌.
    # 리턴을 위한 사이트 주소 저장 함수임
    url_start = 'http://www.10000recipe.com/recipe/'
    url = url_start + str(pagenumber)
    return url