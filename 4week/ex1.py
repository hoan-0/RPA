import pandas as pd

data = {'이름' : ['Kim', 'Park', 'Lee', 'Ho'],
        '국어' : [90, 58, 88, 100],
        '영어' : [100, 60, 80, 70],
        '수학' : [55, 65, 76, 88] }


# 1. 데이터 프레임 생성
df = pd.DataFrame(data)

# 2. 데이터 프레임 출력
print(df, end ="\n\n")

# 3. 학생 이름만 추출해서 출력하시오

sr_name = df['이름']
print(sr_name, end="\n\n")

# 4. 'Park' 성적 출력
park_data = df.loc['Park']
print(park_data, end="\n\n")

# 5. 'Ho' 학생의 수학점수를 90점으로 수정하기
# df.loc[4, 'Ho'] = 90
# print(df.loc[4, ],end="\n\n")
df.loc[df['이름'] == 'Ho', '수학'] = 90
print(df, end="\n\n")

# 6. 'Oh' 학생의 국어(100), 영어(70), 수학(80) 성적을 새로 추가하시오
df.loc[3] = ['Oh', 100, 70, 80]
print(df, end="\n\n")

# 7. 'Lee' 학생의 성적을 삭제하시오.
df = df.drop([2], axis=0)
print(df, end="\n\n")