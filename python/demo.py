import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, lfilter

# 生成包含高频噪声的示例信号
fs = 1000  # 采样率
t = np.arange(0, 1, 1/fs)
signal = np.sin(2 * np.pi * 50 * t) + 0.5 * np.random.randn(len(t))

# 设计巴特沃斯低通滤波器
cutoff_frequency = 100  # 截止频率为100 Hz
order = 4  # 滤波器阶数

b, a = butter(N=order, Wn=cutoff_frequency/(0.5*fs), btype='low', analog=False)

# 应用滤波器
filtered_signal = lfilter(b, a, signal)

# 绘制结果
plt.figure(figsize=(10, 6))

plt.subplot(2, 1, 1)
plt.plot(t, signal, label='原始信号')
plt.title('原始信号')
plt.xlabel('时间 (秒)')
plt.ylabel('幅度')
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(t, filtered_signal, label='滤波后信号', color='orange')
plt.title('低通滤波后信号')
plt.xlabel('时间 (秒)')
plt.ylabel('幅度')
plt.legend()

plt.tight_layout()
plt.show()
