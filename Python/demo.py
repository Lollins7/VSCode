import numpy as np
from scipy.optimize import minimize

# 定义目标函数1


def objective1(x):
    return -(100*x[0] + 90*x[1] + 80*x[2] + 70*x[3])

# 定义目标函数2


def objective2(x):
    return 3*x[1] + 2*x[3]
# 定义联合目标函数（按照权重组合）


def combined_objective(x, alpha=0.5):
    return alpha * objective1(x) + (1 - alpha) * objective2(x)


# 定义约束条件
constraints = ({'type': 'ineq', 'fun': lambda x: np.array([-x[0] - x[1] + 30, -x[2] - x[3] + 30, -3*x[0] - 2*x[2] + 120, -3*x[1] - 2*x[3] + 48]),
                'jac': lambda x: np.array([[-1, -1, 0, 0], [0, 0, -1, -1], [-3, 0, -2, 0], [0, -3, 0, -2]])},
               {'type': 'ineq', 'fun': lambda x: x})  # 添加非负性约束

# 定义初始解
x0 = np.zeros(4)

# 求解多目标规划问题
result = minimize(combined_objective, x0,
                  constraints=constraints, method='SLSQP')

# 显示结果
print("最优解:", result.x)
print("最优z的值：", -objective1(result.x))
print("最优w的值：", objective2(result.x))
print("退出标志:", result.success)
print("迭代信息:", result.message)
