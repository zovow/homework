import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

def visualize_initial_data(dataset):
    """
    可视化原始数据集

    参数:
    - dataset: DataFrame，数据集，包含 'time' 和 'precipitation' 列

    返回:
    - 无，直接显示可视化结果
    """

    # 提取时间和降水量列
    time = dataset['time']
    precipitation = dataset['precipitation']

    # 绘制原始数据的降水量随时间的变化
    plt.figure(figsize=(10, 6))
    plt.plot(time, precipitation, label='Original Precipitation')
    plt.title('Original Precipitation Over Time')
    plt.xlabel('Time')
    plt.ylabel('Precipitation')
    plt.legend()
    plt.show()

def whiten_data(dataset):
    """
    对数据集进行白化处理

    参数:
    - dataset:数据集，包含 'time' 和 'precipitation' 列

    返回:
    - 白化后的数据集
    """

    # 提取降水量列
    precipitation = dataset['precipitation'].values.reshape(-1, 1)

    # 使用 StandardScaler 进行白化处理
    scaler = StandardScaler()
    whitened_precipitation = scaler.fit_transform(precipitation)

    # 替换原始数据集中的降水量列
    dataset['precipitation'] = whitened_precipitation.flatten()

    return dataset

def visualize_whitened_data(dataset):
    """
    可视化白化后的数据集

    参数:
    - dataset:数据集，包含 'time' 和 'precipitation' 列（已白化）

    返回:
    - 无，直接显示可视化结果
    """

    # 提取时间和白化后的降水量列
    time = dataset['time']
    whitened_precipitation = dataset['precipitation']

    # 绘制白化后的降水量随时间的变化
    plt.figure(figsize=(10, 6))
    plt.plot(time, whitened_precipitation, label='Whitened Precipitation')
    plt.title('Whitened Precipitation Over Time')
    plt.xlabel('Time')
    plt.ylabel('Whitened Precipitation')
    plt.legend()
    plt.show()


# 读取 Excel 文件
file_path = 'D:\python-learn\homework_of_week10\data.xlsx'

df = pd.read_excel(file_path)

# 可视化原始数据
visualize_initial_data(df)

# 进行白化处理
whitened_df = whiten_data(df)

# 可视化白化后的数据
visualize_whitened_data(whitened_df)
