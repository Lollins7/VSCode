import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

# 生成非平稳周期时序数据
np.random.seed(0)
t = np.arange(0, 1000)
y1 = np.sin(0.1*t) + np.random.normal(0, 0.5, size=len(t))

# 生成平稳周期时序数据
y2 = np.sin(0.1*t)

# 计算自相关系数
acf1 = sm.tsa.acf(y1, nlags=len(y1))
acf2 = sm.tsa.acf(y2, nlags=len(y2))

# 绘制自相关图
plt.figure(figsize=(10, 4))
plt.stem(range(len(acf1)), acf1, linefmt='r-',
         markerfmt='bo', label='stationary')
plt.stem(range(len(acf2)), acf2, linefmt='b-',
         markerfmt='go', label='Non-Stationary')
plt.xlabel('Lag')
plt.ylabel('Autocorrelation')
plt.title('Autocorrelation Plot')
plt.legend()
plt.grid(True)
plt.show()
