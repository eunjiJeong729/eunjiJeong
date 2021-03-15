#펭수/워크맨 csv 불러와서 시각화 및 머신러닝
# 패키지 import
import datetime as dt
import pandas as pd   #df 분석용
import requests
import time
import urllib.request #
import re
import konlpy

from bs4 import BeautifulSoup
from pandas import DataFrame
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from nltk import FreqDist

# 시각화
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from PIL import Image             #워드클라우드용
from wordcloud import WordCloud   #워드클라우드용
fpath = "NotoSansCJKkr-Bold.otf"   #워드클라우드 국문지원을 위한 별도 폰트 path 설정
%matplotlib inline

# 기계 학습
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC, LinearSVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import Perceptron
from sklearn.linear_model import SGDClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.feature_extraction.text import CountVectorizer

############### Read #################
peng_intro = pd.read_csv('peng_intro.csv')  # 펭수의 intro DF
work_intro = pd.read_csv('work_intro.csv')  # 워크맨의 intro DF

peng = pd.read_csv('peng.csv')  # 펭수의 동영상list DF
peng_reply = pd.read_csv('peng_reply.csv')  # 펭수의 동영상별 댓글list DF

work = pd.read_csv('work.csv')  # 워크맨의 동영상list DF
work_reply = pd.read_csv('work_reply.csv')  # 워크맨의 동영상별 댓글list DF

############# 구분자 추가 ################
for i in range(len(peng)): peng['구분'] = 1  # 펭수 1
for i in range(len(work)): work['구분'] = 0  # 워크맨 0
for i in range(len(peng_reply)): peng_reply['구분'] = 1  # 펭수 1
for i in range(len(work_reply)): work_reply['구분'] = 0  # 워크맨 0

############## DF 통합 ##################
# 1) 펭수 + 워크맨 intro DF 통합
intro_paw = pd.DataFrame(peng_intro)
intro_paw = intro_paw.append(work_intro)

# 2) 펭수 + 워크맨 동영상list DF 통합
paw = pd.DataFrame(peng)
paw = paw.append(work)

# 3) 펭수 + 워크맨 동영상별 댓글list DF 통합
paw_reply = pd.DataFrame(peng_reply)
paw_reply = paw_reply.append(work_reply)

intro_paw.info()

paw = paw.astype({'좋아요': int},{'싫어요':int},{'댓글수':int}) #int형 재확인
paw.describe()  #  통합한 동영상list DF 확인

paw_reply.info()  # 통합한 동영상별 댓글list DF 확인
paw.info()
intro_paw.head()

from matplotlib import font_manager, rc

fig = plt.figure(figsize=(20,5))
plt.title('가장 많은 좋아요 순 정렬')
sns.barplot(x='제목', y='좋아요', data=paw[['제목', '좋아요']].groupby('제목', as_index=False).mean().sort_values(by='좋아요', ascending=False));
plt.xticks(rotation=90); #x축(country) 회전
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)

# 구분에 따른 요약 빈도 차트
paw[['좋아요','구분']].groupby('구분', as_index=False).mean().sort_values(by='좋아요', ascending=False).head()

############ UNLIKE RATIO 구하기 ############  
# 워킹맨 구독자 수가(353만명) 펭수(134만명)의 3배이상으로, 
# 비율을 구해 서로의 값을 확인 예정

unlike_ratio_list = []
for i in range(len(paw)): 
    unlike_ratio = (paw.iloc[i, 5] / paw.iloc[i,4]) * 100  # 퍼센테이지 표현
    unlike_ratio_ar= round(unlike_ratio,2)                 # 소숫점 2자리까지 표현 
    unlike_ratio_list.append(unlike_ratio_ar)          

paw['unlike_ratio(%)'] = unlike_ratio_list                 # ratio 열 생성

paw.head()
paw_reply.head()

# unlike에 따른 정렬 및 시각화
peng_list = []  # 현재 df가 통합되어, 색상 분리를 위해 다시 분리
work_list = []

for i in range(len(paw)):
    if (paw.iloc[i, 8]) == 1:  # '구분'이 펭수일 경우
        peng = paw.iloc[i, 9]  # 펭수의 ratio를 peng_list에 삽입
        peng_list.append(peng)
    else:
        work = paw.iloc[i, 9]  # '구분'이 워크맨일 경우
        work_list.append(work)  # 워크맨의 ratio를 work_list에 삽입

plt.plot(peng_list, marker='.', color='b')  # 펭수: blue
plt.plot(work_list, marker='.', color='r')  # 워크맨: red
plt.legend(['펭수', '워크맨'], loc='upper right')

# 구분에 따른 요약
paw[['unlike_ratio(%)', '구분']].groupby('구분', as_index=False).mean().sort_values(by='unlike_ratio(%)', ascending=False).head()

# 워드 클라우드 설정
title_l2s=(''.join(paw["제목"])) # paw의 제목df를 string으로

image_test=np.array(Image.open("ytbb.png")) #mask 이미지 설정
wc = WordCloud(max_font_size=200,font_path=fpath,background_color='#FFFFFF', width=1200,height=800,mask=image_test).generate(title_l2s)

#사이즈 등 설정
plt.figure(figsize=(10,8))
plt.imshow(wc)
plt.tight_layout(pad=0)
plt.axis('off')

total_cnt = len(paw_reply['ID'])
cnt_1percent= total_cnt*0.01
print("* 전체 댓글 개수:", len(paw_reply['ID']), ", 전체 댓글의 1% 개수:", cnt_1percent)
print("/////////////////////////////////////////////////////////////////////////////")
print("* 상위 10% User ID 빈도수 확인(count):")
print(paw_reply['ID'].value_counts(ascending=False)[:31]) # 빈도수 기준 내림차순

print("/////////////////////////////////////////////////////////////////////////////")
print("* 상위 10% User 빈도수 확인(ratio):")
print(paw_reply['ID'].value_counts(normalize=True)[:31])  # 비율 기준 출력

# csv 파일의 columnms 확인
paw.columns
paw_reply.columns

# csv 파일에서 필요한 column만 리스트로 저장
paw_title_list = paw.제목.tolist()
paw_content_list = paw.본문내용.tolist()
paw_reply_list = paw_reply.Comment.tolist()

# 리스트 출력하여 확인
print(paw_title_list[:3])  #부하로 인해 테스트로 3개만 출력

# 형태소 분석
from konlpy.tag import Okt
okt=Okt()

# 제목 리스트 명사 분석
title_list = []
for i in range(len(paw_title_list)):
    title_list.append(okt.nouns(paw_title_list[i]))

# 본문 내용 명사 분석
content_list = []
for i in range(len(paw_content_list)):
    content_list.append(okt.nouns(paw_content_list[i]))

# 댓글 내용 명사 분석
reply_list = []
for i in range(len(paw_reply_list)):
    reply_list.append(okt.nouns(paw_reply_list[i]))

# 리스트 안의 리스트 하나의 리스트로 만들기
def flatten (n):
    org =[]
    for i in n :
        if (isinstance(i,list)):
            org += flatten(i)
        else:
            org.append(i)
    return org


flatten(title_list) # 실행되는지 확인

# 제목, 본문 내용, 댓글 내용 하나의 리스트로 취합
title_f = flatten(title_list)
content_f = flatten(content_list)
reply_f = flatten(reply_list)

# 단어 빈도수 확인을 위한 패키지 import
from nltk.book import *
import operator
from nltk.corpus import brown
from nltk.corpus import stopwords

# 제목 빈도수 확인
fdist1 = FreqDist(title_f)
title_dict = {}
content_dict = {}
reply_dict = {}

dict_w = {}
for w in title_f:
    dict_w[w] = fdist1[w]
title_dict = sorted(dict_w.items(), key=operator.itemgetter(1), reverse=True)
print(title_dict)

# 본문 내용 빈도수 확인
fdist1 = FreqDist(content_f)
dict_w = {}
for w in content_f:
    dict_w[w] = fdist1[w]
content_dict = sorted(dict_w.items(), key=operator.itemgetter(1), reverse=True)
print(content_dict)

# 댓글 내용 빈도수 확인
fdist1 = FreqDist(reply_f)
dict_w = {}
for w in reply_f:
    dict_w[w] = fdist1[w]
reply_dict = sorted(dict_w.items(), key=operator.itemgetter(1), reverse=True)
print(reply_dict)

# 빈도수를 데이터프레임 형태로 저장
title_df = DataFrame(title_dict)
content_df = DataFrame(content_dict)
reply_df = DataFrame(reply_dict)

title_df.head() # 데이터 확인


####### Machine Learning #################
data = paw
data.head()

print ("Data shape:", paw.shape, "\n")
print (data.info())

data.drop('제목', axis=1, inplace=True)    # 무의미
data.drop('주소', axis=1, inplace=True)    # 무의미
data.drop('조회수', axis=1, inplace=True)  #120만 넘을경우, python에서 처리 못함
data.drop('댓글수', axis=1, inplace=True)  # object
data.drop('좋아요', axis=1, inplace=True)  # unlike_ratio 속성과 성격 동일
data.drop('싫어요', axis=1, inplace=True)  # unlike_ratio 속성과 성격 동일
data.drop('본문내용', axis=1, inplace=True) # 무의미

data.head()

# train / test data를 임의로 나누기 위해 댓글 수로 정렬 시도
data = data.sort_values(by='unlike_ratio(%)', ascending=True)
data.head()

# test / train data 분리
rows_count=len(data)   # train : test data를 7:3으로 나누기위한 수
print("Total-data:",rows_count)           # 158

train_rows = int(rows_count*0.7); # train data는 70% = 110
test_rows = int(rows_count*0.3);  # test data는 30% = 47

data_train = data[:train_rows]
data_test = data[train_rows:rows_count]
print("실제로 나눠진 수:", "(Train)",len(data_train), "(Test)",len(data_test)) # 첫자리 포함하기 때문

# 나눠진 data 확인
print ("Data_train shape:", data_train.shape, "\n")
print ("Data_test shape:", data_test.shape, "\n")
print (data_train.info())
print('_'*40)
print (data_test.info())

X_train = data_train.drop("구분", axis=1) # x_train에서는 '구분' 없이 예측
Y_train = data_train["구분"]              # y_train은 결과값 뿐이므로

X_test = data_test.drop("구분" , axis=1).copy()
print("X_train:", X_train.shape, ", Y_train:", Y_train.shape, ", X_test:", X_test.shape)

# 1. Logistic Regression
logreg = LogisticRegression(solver='lbfgs')
logreg.fit(X_train, Y_train)

type(X_train)
type(Y_train)

Y_pred = logreg.predict(X_test)
acc_log= round(logreg.score(X_train, Y_train) * 100, 2)
acc_log

# 2. Support Vector Machines
svc = SVC()
solver='liblinear'
svc.fit(X_train, Y_train)

Y_pred = svc.predict(X_test)
acc_svc = round(svc.score(X_train, Y_train) * 100, 2)
print(acc_svc)

# 3. Decision Tree
decision_tree = DecisionTreeClassifier()
decision_tree.fit(X_train, Y_train)
Y_pred = decision_tree.predict(X_test)
acc_decision_tree = round(decision_tree.score(X_train, Y_train) * 100, 2)
acc_decision_tree

# 4. KNN
knn = KNeighborsClassifier(n_neighbors = 3)
knn.fit(X_train, Y_train)
Y_pred = knn.predict(X_test)
acc_knn = round(knn.score(X_train, Y_train) * 100, 2)
acc_knn

# 5. Gaussian Naive Bayes
gaussian = GaussianNB()
gaussian.fit(X_train, Y_train)
Y_pred = gaussian.predict(X_test)
acc_gaussian = round(gaussian.score(X_train, Y_train) * 100, 2)
acc_gaussian

# 6. Linear SVC
linear_svc = LinearSVC()
linear_svc.fit(X_train, Y_train)
Y_pred = linear_svc.predict(X_test)
acc_linear_svc = round(linear_svc.score(X_train, Y_train) * 100, 2)
acc_linear_svc

# 7. Perceptron
perceptron = Perceptron()
perceptron.fit(X_train, Y_train)
Y_pred = perceptron.predict(X_test)
acc_perceptron = round(perceptron.score(X_train, Y_train) * 100, 2)
acc_perceptron

# 8. Random Forest
random_forest = RandomForestClassifier(n_estimators=100)
random_forest.fit(X_train, Y_train)
Y_pred = random_forest.predict(X_test)
random_forest.score(X_train, Y_train)
acc_random_forest = round(random_forest.score(X_train, Y_train) * 100, 2)
acc_random_forest

# 9. Stochastic Gradient Descent
sgd = SGDClassifier()
sgd.fit(X_train, Y_train)
Y_pred = sgd.predict(X_test)
acc_sgd = round(sgd.score(X_train, Y_train) * 100, 2)
acc_sgd

models = pd.DataFrame({
    'Model': ['Support Vector Machines', 'KNN', 'Logistic Regression', 'Random Forest', 'Naive Bayes', 'Perceptron', 'Stochastic Gradient Decent', 'Linear SVC', 'Decision Tree'],
    'Score': [acc_svc, acc_knn, acc_log, acc_random_forest, acc_gaussian, acc_perceptron, acc_sgd, acc_linear_svc, acc_decision_tree]})
models.sort_values(by='Score', ascending=False)

submission = pd.DataFrame({
        "Unlike_ratio(%)": data_test["unlike_ratio(%)"], "구분(펭수:1/워크맨:0)": Y_pred
    })
submission.to_csv('2019_TextMining_Team_num_4.csv', mode='w', encoding="utf-8-sig", index=False)

# 결과 요약
data_final = pd.read_csv('2019_TextMining_Team_num_4.csv')
data_final.info()
data_final.describe()