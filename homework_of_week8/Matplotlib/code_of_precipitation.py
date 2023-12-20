import pandas as pd
import matplotlib.pyplot as plt

# 读取Excel文件
df = pd.read_excel("D:\data.xlsx")

# 提取时间和降水量列
time = df['time']
precipitation = df['precipitation']

point_size = 1
# 1. 折线图
plt.figure(figsize=(12, 4))
plt.subplot(1, 3, 1)
plt.plot(time, precipitation, marker='o', markersize=point_size, linestyle='-', color='b')
plt.xlabel('time')
plt.ylabel('precipitation/mm')
plt.title('Line Plot')

# 2. 散点图
plt.subplot(1, 3, 2)
plt.scatter(time, precipitation, s=point_size, color='green')
plt.xlabel('time')
plt.ylabel('precipitation/mm')
plt.title('Scatter Plot')

# 3. 柱状图
plt.subplot(1, 3, 3)
plt.bar(time, precipitation, color='orange', alpha=0.7)
plt.xlabel('time')
plt.ylabel('precipitation/mm')
plt.title('Bar Chart')
plt.ylim(0, 200)  # 设置y轴范围，最大值为300

# 调整布局并显示图形
plt.tight_layout()
plt.show()