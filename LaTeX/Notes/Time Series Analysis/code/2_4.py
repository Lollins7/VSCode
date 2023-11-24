import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 创建具有一半数据在x轴上方，一半在x轴下方的示例时间序列数据
n = 100
half_n = n // 2

# 创建递增部分
increasing_data = np.arange(1, half_n + 1)

# 创建递减部分
decreasing_data = np.arange(half_n, 0, -1)

# 合并数据
data = np.concatenate((increasing_data, decreasing_data))

# 添加随机噪声
data_with_noise = data + np.random.normal(0, 1, n)

# 创建年份范围
years = pd.date_range(start='1978', periods=n, freq='Y')

# 创建DataFrame
data_df = pd.DataFrame({'Year': years, 'Trend_Data': data_with_noise})
data_df.set_index('Year', inplace=True)

# 绘制递增趋势的时序图
plt.figure(figsize=(10, 5))
plt.plot(data_df.index, data_df['Trend_Data'], marker='o')
plt.title('Time Series with Increasing Trend')
plt.xlabel('Year')
plt.ylabel('Value')
plt.grid(True)

# 计算自相关系数
autocorr = [1.0]
for lag in range(1, n):
    corr = np.corrcoef(data_df['Trend_Data'][:-lag],
                       data_df['Trend_Data'][lag:])[0, 1]
    autocorr.append(corr)

# 绘制自相关图
plt.figure(figsize=(10, 5))
plt.stem(range(n), autocorr, markerfmt='ro', basefmt='b-')
plt.title('Autocorrelation Plot of Time Series with Increasing Trend')
plt.xlabel('Lag (Years)')
plt.ylabel('Autocorrelation')
plt.grid(True)
plt.show()
