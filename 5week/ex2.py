import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager



def addtext(x, y, z):
    for i in range(len(x)):
        plt.text(i, y[i] + 0.5, f'{y[i]} ({z[i]})', ha='center')


hat = pd.read_csv('singer_youtube.csv')
print(hat.head(), end="\n\n")

font_path = "/Users/jeonghwan-yeong/SHU/RPA/5week/malgun.ttf"
font_name = font_manager.FontProperties(fname=font_path).get_name()
plt.rc('font', family='AppleGothic')  # macOS 기본 폰트 사용

plt.figure(figsize=(15, 10))
plt.bar(hat['name'], hat['youtube count'], color = ('red','orange','yellow','green','blue','navy','purple'))
plt.title('youtube count by')
plt.xlabel('name')
plt.ylabel('youtube count')

addtext(hat['name'], hat['youtube count'], hat['address'])


plt.show()
