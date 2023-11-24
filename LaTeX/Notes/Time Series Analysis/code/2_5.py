import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

# 生成平稳周期时序数据
np.random.seed(0)
t = np.arange(0, 1000)
y = np.sin(0.1*t)

# 绘制时序图
plt.figure(figsize=(10, 4))
plt.plot(t, y)
plt.xlabel('Time')
plt.ylabel('Value')
plt.title('Stationary Periodic Time Series')
plt.grid(True)
plt.show()

# 计算自相关系数
acf = sm.tsa.acf(y, nlags=len(y))

# 绘制自相关图
plt.figure(figsize=(10, 4))
plt.stem(range(len(acf)), acf)
plt.xlabel('Lag')
plt.ylabel('Autocorrelation')
plt.title('Autocorrelation Plot')
plt.grid(True)
plt.show()
