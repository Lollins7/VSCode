# 安装和加载必要的包（如果尚未安装的话）
# install.packages("ggplot2")
library(ggplot2)

# 设置正太分布的均值和标准差
mean_value <- 1 # 均值大于0
sd_value <- 1 # 标准差

# 生成正太分布的数据
x <- seq(-3, 5, 0.01) # 定义x的范围
y <- dnorm(x, mean = mean_value, sd = sd_value) # 计算密度值

# 创建ggplot对象并画密度曲线
plot <- ggplot(data = data.frame(x = x, y = y), aes(x = x, y = y)) +
    geom_line(color = "black", size = 1) + # 画黑色实线密度曲线
    geom_vline(xintercept = 0, color = "black", size = 1, linetype = "solid", arrow = arrow()) + # 画黑色实线x=0的竖线，带箭头
    geom_hline(yintercept = 0, color = "black", size = 1, linetype = "solid", arrow = arrow()) + # 画黑色实线y=0的横线，带箭头
    theme_void() # 不显示坐标轴和标签

# 显示图形
print(plot)
