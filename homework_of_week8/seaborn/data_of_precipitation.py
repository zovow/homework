import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 读取Excel文件
df = pd.read_excel("D:\data.xlsx")

# 设置图形风格
sns.set(style="whitegrid")

# 设置每一个数据点的大小
point_size = 2

# 1. 折线图
plt.figure(figsize=(12, 4))
plt.subplot(1, 3, 1)
sns.lineplot(x='time', y='precipitation', data=df, marker='o', markersize=point_size, color='b')
plt.xlabel('time')
plt.ylabel('precipitation/mm')
plt.title('Line Plot')

# 2. 散点图
plt.subplot(1, 3, 2)
sns.scatterplot(x='time', y='precipitation', data=df, s=point_size, color='green')
plt.xlabel('time')
plt.ylabel('precipitation/mm')
plt.title('Scatter Plot')

# 3. 柱状图
plt.subplot(1, 3, 3)
sns.barplot(x='time', y='precipitation', data=df, color='orange', alpha=0.7)
plt.xlabel('time')
plt.ylabel('precipitation/mm')
plt.title('Bar Chart')

# 显示图形
plt.tight_layout()
plt.show()

