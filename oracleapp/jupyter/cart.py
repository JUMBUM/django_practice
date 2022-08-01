
# 데이터 처리하는 라이브러리 사용하기..
import pandas as pd

# 오라클 연결, 접속, SQL 구문 처리 라이브러리
# 먼저 prompt에서 설치 : conda install -c conda-forge cx_Oracle
import cx_Oracle 

# 오라클 연결하기
dsn=cx_Oracle.makedsn('localhost',1521,'xe') 
print(dsn)

# 오라클 접속하기
conn=cx_Oracle.connect('korhrd','dbdb', dsn)
conn

# <데이터베이스 사용 방법>

# 1. 데이터베이스와 소통할 객체 생성
# 2. SQL 구문을 커서에 실어서 오라클에 전달하면,
# 3. 오라클이 SQL구문을 처리한 후,
# 4. 결과값을 커서에 실어서 보내준다.
# 5. 연결끊기

# 1. 데이터베이스와 소통할 객체 생성
cursor=conn.cursor() 


# 2. SQL 구문을 커서에 실어서 오라클에 전달(Execute)하면,
# 3. 오라클이 SQL구문을 처리한 후,

sql = """select * from cart"""

cursor.execute(sql) 

# 4. 결과값을 커서에 실어서 보내준다.
# 리스트 형태로 모든 데이터 읽어오기..
row=cursor.fetchall() 
print(row)


# 4. 결과값을 커서에 실어서 보내준다.
# 컬럼 이름 확인하기
colname=cursor.description
print(colname)

# 5. cursor를 닫은 다음, DB와의 연결을 끊어준다
# 커서 반납하기
cursor.close()

# DB와의 접속 끊기
conn.close()

col=[] 
for i in colname: 
    col.append(i[0]) 

print(col)

# pandas를 사용한 데이터 프레임 형식으로 변환 
emp=pd.DataFrame(row, columns=col) 
print(emp)