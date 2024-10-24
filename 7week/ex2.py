import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('2024_seoul_data.csv', encoding='utf-8')
df2 = df.fillna(method='ffill')
df2.info()

df2.rename(columns={'일강수량':'rain'}, inplace=True)
df2.head(2)

plt.rc('font', family='AppleGothic')  # macOS 기본 폰트 사용
plt.rcParams['axes.unicode_minus'] = False

plt.title('서울시 2024년도 일수별 여름 강수량')
plt.plot(df2['일시'], df2['rain'],label='강수량',c='r')

plt.xlabel('일수')
plt.ylabel('강수량')
plt.legend()
plt.show()