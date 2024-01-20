import requests
from bs4 import BeautifulSoup
import re

import mod1

class Recipe:
    # 레시피를 저장시키기 위한 클래스 틀 생성
    # 사이트의 마지막 페이지넘버를 number 변수에 저장
    # mod1 파일에 작성된 함수들을 import하여 각 변수에 저장
    def getdata(self, number):
        self.number = number # 주소 확인을 위한 변수. 변수에는 주소값 마지막 숫자가 저장됨
        self.el = mod1.getel(number) # 요리 재료를 저장하는 변수. 형식은 딕셔너리임
        self.name = mod1.getrecipe_name(number) # 요리 이름을 저장하는 변수
        self.time = mod1.getrecipe_time(number) # 소요시간을 저장하는 변수
        self.level = mod1.getrecipe_level(number) # 난이도을 저장하는 변수
        self.recipeurl = mod1.shpwrecipe_descrip(number) # 레시피의 사이트를 저장하는 변수
        self.count = 0 # 사용자가 가지고 있는 재료와 레시피의 재료수를 비교하기 위한 count 변수임
        return

# 여기부터는 객체 생성 진행. 객체는 각각의 레시피이며 레시피는 총 6개의 레시피북에 각각 나누어져 군집화 되어있음
# for문으로 객체를 생성함. 레시피 사이트에서 인기도 위주로 레시피 객체를 생성함. 약 250개의 레시피 객체 생성
name1_re = []
j = 0
for i in range(6900101, 6900141):
    namesub = 'recipeob' + str(i)
    name1_re.append(namesub)
    name1_re[j] = Recipe()
    name1_re[j].getdata(i)
    j = j + 1
name2_re = []
j = 0
for i in range(6900351, 6900421):
    namesub = 'recipeob' + str(i)
    name2_re.append(namesub)
    name2_re[j] = Recipe()
    name2_re[j].getdata(i)
    j = j + 1
name3_re = []
j = 0
for i in range(6900481, 6900511):
    namesub = 'recipeob' + str(i)
    name3_re.append(namesub)
    name3_re[j] = Recipe()
    name3_re[j].getdata(i)
    j = j + 1
name4_re = []
j = 0
for i in range(6900521, 6900561):
    namesub = 'recipeob' + str(i)
    name4_re.append(namesub)
    name4_re[j] = Recipe()
    name4_re[j].getdata(i)
    j = j + 1
name5_re = []
j = 0
for i in range(6900571, 6900601):
    namesub = 'recipeob' + str(i)
    name5_re.append(namesub)
    name5_re[j] = Recipe()
    name5_re[j].getdata(i)
    j = j + 1
name6_re = []
j = 0
for i in range(6900641, 6900681):
    namesub = 'recipeob' + str(i)
    name6_re.append(namesub)
    name6_re[j] = Recipe()
    name6_re[j].getdata(i)
    j = j + 1

# 여기부터는 사용자 인터렉션이 들어감
# 사용자에게 본인이 가지고 있는 재료를 받음
userdata_re = input("현재 가지고 있는 재료를 입력하세요 : ")
userdata = userdata_re.split() # 입력 받은 재료를 split하여 리스트에 저장

# 사용자에게 입력 받은 재료를 각 레시피북의 레시피 재료수와 비교
# receipBook1부터 6까지 반복하여 진행
receipBook1 = {}
minusN1 = []
for i in range(0, 40):  # 0부터 40까지의 레시피가 있음
    for j in userdata:  # 사용자에게 받은 재료 모음 ex.두부 쪽파 계란 간장 김치 소금 밥
        if j in name1_re[i].el.keys():  # 크롤링한 레시피의 재료가 저장된 딕셔너리 키값들
            name1_re[i].count = name1_re[i].count + 1  # 딕셔너리에 재료가 있으면 +1
    minusN1.append(len(name1_re[i].el.keys()) - name1_re[i].count) # 레시피속 재료개수 - 사용자 재료 개수
    receipBook1_s = {i: minusN1[i]}
    # 레시피북 속 레시피의 넘버링을 key로, 그 레시피의 재료개수 - 사용자 재료 개수를 value로 가지는 딕셔너리를 저장
    receipBook1.update(receipBook1_s)

receipBook2 = {}
minusN2 = []
for i in range(0, 70):
    for j in userdata:
        if j in name2_re[i].el.keys():
            name2_re[i].count = name2_re[i].count + 1
    minusN2.append(len(name2_re[i].el.keys()) - name2_re[i].count)
    receipBook2_s = {i: minusN2[i]}
    receipBook2.update(receipBook2_s)

receipBook3 = {}
minusN3 = []
for i in range(0, 30):
    for j in userdata:
        if j in name3_re[i].el.keys():
            name3_re[i].count = name3_re[i].count + 1
    minusN3.append(len(name3_re[i].el.keys()) - name3_re[i].count)
    receipBook3_s = {i: minusN3[i]}
    receipBook3.update(receipBook3_s)

receipBook4 = {}
minusN4 = []
for i in range(0, 40):
    for j in userdata:
        if j in name4_re[i].el.keys():
            name4_re[i].count = name4_re[i].count + 1
    minusN4.append(len(name4_re[i].el.keys()) - name4_re[i].count)
    receipBook4_s = {i: minusN4[i]}
    receipBook4.update(receipBook4_s)

receipBook5 = {}
minusN5 = []
for i in range(0, 30):
    for j in userdata:
        if j in name5_re[i].el.keys():
            name5_re[i].count = name5_re[i].count + 1
    minusN5.append(len(name5_re[i].el.keys()) - name5_re[i].count)
    receipBook5_s = {i: minusN5[i]}
    receipBook5.update(receipBook5_s)

receipBook6 = {}
minusN6 = []
for i in range(0, 40):
    for j in userdata:
        if j in name6_re[i].el.keys():
            name6_re[i].count = name6_re[i].count + 1
    minusN6.append(len(name6_re[i].el.keys()) - name6_re[i].count)
    receipBook6_s = {i: minusN6[i]}
    receipBook6.update(receipBook6_s)

# 여기부터는 레시피북과 그 안의 레시피 중 가장 적합한 재료를 가진 레시피를 추출하기 위한 작업임
# 1. 위에서 비교한 데이터를 가지고 각각의 receipBook 속 가장 작은수를 가진 레시피를 추출함
mindex1 = 0 # 레시피북 속 미니멈 숫자를 저장하기 위한 변수
for i in range(0, len(receipBook1)): #0부터 40
    value_s = receipBook1.values()
    value = list(value_s) # 딕셔너리의 벨류값 중 미니멈을 구하기 위해 리스트로 형변환
    mindex1 = min(value) # 리스트 중 미니멈 확인
    reindex1 = value.index(mindex1) # 마지막에 레시피를 호출하기 위한 인덱스 값 저장

# 2. 토탈미니멈 : 6개 레시피의 미니멈을 저장하기 위한 딕셔너리
totalminimum = {}
totalminimum_s = {1: mindex1}
totalminimum.update(totalminimum_s) # 1번째 북

mindex2 = 0
for i in range(0, len(receipBook2)):
    value_s = receipBook2.values()
    value = list(value_s)
    mindex2 = min(value)
    reindex2 = value.index(mindex2)

# 2. 토탈미니멈 : 6개 레시피의 미니멈을 저장하기 위한 딕셔너리
totalminimum_s = {2: mindex2}
totalminimum.update(totalminimum_s) # 2번째 북

mindex3 = 0
for i in range(0, len(receipBook3)):
    value_s = receipBook3.values()
    value = list(value_s)
    mindex3 = min(value)
    reindex3 = value.index(mindex3)

# 2. 토탈미니멈 : 6개 레시피의 미니멈을 저장하기 위한 딕셔너리
totalminimum_s = {3: mindex3}
totalminimum.update(totalminimum_s) # 3번째 북

mindex4 = 0
for i in range(0, len(receipBook4)):
    value_s = receipBook4.values()
    value = list(value_s)
    mindex4 = min(value)
    reindex4 = value.index(mindex4)

# 2. 토탈미니멈 : 6개 레시피의 미니멈을 저장하기 위한 딕셔너리
totalminimum_s = {4: mindex4}
totalminimum.update(totalminimum_s) # 4번째 북

mindex5 = 0
for i in range(0, len(receipBook5)):
    value_s = receipBook5.values()
    value = list(value_s)
    mindex5 = min(value)
    reindex5 = value.index(mindex5)

# 2. 토탈미니멈 : 6개 레시피의 미니멈을 저장하기 위한 딕셔너리
totalminimum_s = {5: mindex5}
totalminimum.update(totalminimum_s) # 5번째 북

mindex6 = 0
for i in range(0, len(receipBook6)):
    value_s = receipBook6.values()
    value = list(value_s)
    mindex6 = min(value)
    reindex6 = value.index(mindex6)

# 2. 토탈미니멈 : 6개 레시피의 미니멈을 저장하기 위한 딕셔너리
totalminimum_s = {6: mindex6}
totalminimum.update(totalminimum_s) # 6번째 북

# 3. receipBook들 간의 경쟁
for i in range(1, 7): # 6개의 미니멈 중에서도 최종 1개 고르기
    totlavalue_s = totalminimum.values()
    totalvalue = list(totlavalue_s) # 딕셔너리의 벨류값 중 미니멈을 구하기 위해 리스트로 형변환
    totalindex = min(totalvalue) # 리스트 중 미니멈 확인
    totalreindex = totalvalue.index(totalindex)

# 4. 최종 출력
# receipBook중 가장 적합한 것과 그 안에 있는 레시피 중 가장 적합한 것을 프린팅함
if(totalreindex == 0):
    print("지금 만들 수 있는 요리는 : ", name1_re[reindex1].name)
    print("\n요리의 난이도는 : ", name1_re[reindex1].level)
    print("\n소요시간은 : ", name1_re[reindex1].time)
    user = input("자세한 조리 과정을 알고싶으시면 Y를 입력하세요 : ")
    # 사용자 인터렉션 추가
    if user == 'Y':
        print("\n해당 주소로 검색하면 자세한 조리과정을 볼 수 있습니다. 맛있는 음식 만드세요 : ", name1_re[reindex1].recipeurl)
    else :
        print("프로그램을 종료합니다.")
elif(totalreindex == 1):
    print("지금 만들 수 있는 요리는 : ", name2_re[reindex2].name)
    print("\n요리의 난이도는 : ", name2_re[reindex2].level)
    print("\n소요시간은 : ", name2_re[reindex2].time)
    user = input("자세한 조리 과정을 알고싶으시면 Y를 입력하세요 : ")
    if user == 'Y':
        print("\n해당 주소로 검색하면 자세한 조리과정을 볼 수 있습니다. 맛있는 음식 만드세요 : ", name2_re[reindex2].recipeurl)
    else :
        print("프로그램을 종료합니다.")
elif (totalreindex == 2):
    print("지금 만들 수 있는 요리는 : ", name3_re[reindex3].name)
    print("\n요리의 난이도는 : ", name3_re[reindex3].level)
    print("\n소요시간은 : ", name3_re[reindex3].time)
    user = input("자세한 조리 과정을 알고싶으시면 Y를 입력하세요 : ")
    if user == 'Y':
        print("\n해당 주소로 검색하면 자세한 조리과정을 볼 수 있습니다. 맛있는 음식 만드세요 : ", name3_re[reindex3].recipeurl)
    else :
        print("프로그램을 종료합니다.")
elif (totalreindex == 3):
    print("지금 만들 수 있는 요리는 : ", name4_re[reindex4].name)
    print("\n요리의 난이도는 : ", name4_re[reindex4].level)
    print("\n소요시간은 : ", name4_re[reindex4].time)
    user = input("자세한 조리 과정을 알고싶으시면 Y를 입력하세요 : ")
    if user == 'Y':
        print("\n해당 주소로 검색하면 자세한 조리과정을 볼 수 있습니다. 맛있는 음식 만드세요 : ", name4_re[reindex4].recipeurl)
    else :
        print("프로그램을 종료합니다.")
elif (totalreindex == 4):
    print("지금 만들 수 있는 요리는 : ", name5_re[reindex5].name)
    print("\n요리의 난이도는 : ", name5_re[reindex5].level)
    print("\n소요시간은 : ", name5_re[reindex5].time)
    user = input("자세한 조리 과정을 알고싶으시면 Y를 입력하세요 : ")
    if user == 'Y':
        print("\n해당 주소로 검색하면 자세한 조리과정을 볼 수 있습니다. 맛있는 음식 만드세요 : ", name5_re[reindex5].recipeurl)
    else :
        print("프로그램을 종료합니다.")
elif (totalreindex == 5):
    print("지금 만들 수 있는 요리는 : ", name6_re[reindex6].name)
    print("\n요리의 난이도는 : ", name6_re[reindex6].level)
    print("\n소요시간은 : ", name6_re[reindex6].time)
    user = input("자세한 조리 과정을 알고싶으시면 Y를 입력하세요 : ")
    if user == 'Y':
        print("\n해당 주소로 검색하면 자세한 조리과정을 볼 수 있습니다. 맛있는 음식 만드세요 : ", name6_re[reindex6].recipeurl)
    else :
        print("프로그램을 종료합니다.")