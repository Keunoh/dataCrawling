import pandas as pd

# csv파일 불러오기
df1 = pd.read_csv('../csv/hospital.csv', encoding='utf-8')

# 해당 csv의 컬럼명을 추출하기
# print(df1.info())

# 해당 csv의 컬럼명 추출하기(리스트형식)
# print(df1.columns.values)

# 원하는 컬럼만 추출하기(모든행 추출)
x_data = df1[['요양기관명', '시군구코드', '주소', '전화번호', 'x좌표', 'y좌표']]
print(x_data.head())

# 데이터 필터링 후 원하는 위치에 csv파일로 dataframe을 저장
x_data.to_csv('../csv/modified_hospital.csv')
