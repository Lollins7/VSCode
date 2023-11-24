import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

# 生成平稳时间序列数据
np.random.seed(0)
t = np.arange(0, 100)
y = np.random.normal(0, 1, size=len(t))

# 绘制时序图
plt.figure(figsize=(10, 4))
plt.plot(t, y)
plt.xlabel('Time')
plt.ylabel('Value')
plt.title('Time Series Plot')
plt.grid(True)
plt.show()

# 计算自相关系数
acf = sm.tsa.acf(y, nlags=len(y))

# 绘制自相关图
plt.figure(figsize=(10, 4))
plt.stem(range(len(acf)), acf, linefmt='r-', markerfmt='ro', basefmt='r-')
plt.xlabel('Lag')
plt.ylabel('Autocorrelation')
plt.title('Autocorrelation Plot')
plt.grid(True)
plt.show()
