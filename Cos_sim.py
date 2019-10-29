import numpy as np
import pandas as pd

df = pd.read_csv("test_data/data_ori2.csv")    #원본파일
df1 = pd.read_csv("test_data/data_created.csv")   #비식별파일

#일련번호순으로 정렬
s_df = df.sort_values(by='일련번호') #index는 일련번호의미
s_df1 = df1.sort_values(by='일련번호')

#컬럼지정
interest_column = pd.Series(['신용대출한도','월소득']) #원하는 열 선택

#삭제된 행 처리
deleted_rows = list(set(s_df['일련번호']) - set(s_df1['일련번호']))
deleted_rows.sort()

j=0
count = -1
deleted_index=[]
    #삭제된 행은 원본에서도 삭제
for i in s_df['일련번호']:
    count = count + 1
    if i == deleted_rows[j]:
        deleted_index.append(count)
        j = j + 1
        if j>k:
            break
        continue
s_df = s_df.drop(deleted_index)

#컬럼별 연산

cos = {}
for i in interest_column:
    dot = np.dot(df[i], df1[i])
    norma = np.linalg.norm(df[i])
    normb = np.linalg.norm(df1[i])
    cos[i] = dot / (norma * normb)

#컬럼별 결과 출력
cos

#최적의 결과 제공
