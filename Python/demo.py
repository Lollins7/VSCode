from sympy import symbols, sin, series

# 定义符号变量
x = symbols('x')

# 定义要展开的函数
f = sin(x)

# 计算函数的泰勒展开
taylor_series = series(f, x, 0, 10)  # 在x=0处展开，展开到5阶

# 打印结果
print(taylor_series)
