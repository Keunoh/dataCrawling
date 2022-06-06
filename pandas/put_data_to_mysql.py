# 1
import pandas as pd
import pymysql
from sqlalchemy import create_engine

# pymysql 세팅
db = pymysql.connect(user='root', host='localhost', passwd='mysql', port=3306, db='firstdb')
cursor = db.cursor()

# csv파일 불러오기
df = pd.read_csv('../csv/modified_hospital.csv', encoding='utf-8-sig')
# df.columns = ['테이블과 동일한 컬럼명 사용하도록 수정']

# sqlalchemy를 사용해 원하는 database에 csv파일 저장
engine = create_engine("mysql+pymysql://root:"+"mysql"+"@localhost:3306/firstdb?charset=utf8", encoding = "utf-8")
conn = engine.connect()
df.to_sql(name="seconddb", con=engine, index=False)
conn.close()

# 저장 확인
sql = "select * from firstdb limit 5"
pd.read_sql(sql, db)