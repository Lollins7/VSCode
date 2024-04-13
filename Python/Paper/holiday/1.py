import numpy as np
import matplotlib.pyplot as plt

plt.rc('text', usetex=True)
np.random.seed(0)

T = 20
dt = 0.001

t = np.arange(0, T, dt)
x = np.zeros((10, len(t)+1))
y = np.zeros((50, len(t)+1))
v = np.zeros((10, len(t)+1))
rho = np.zeros((10, len(t)+1))
x[:, 0] = np.array([[2.5, -2.5, 0, 2, 4, 5, 0.5, -4, -3.5, -2.5]])
y[:, 0] = np.kron([[1]*5],x[:, 0])
rho[:, 0] = np.random.rand(10, 1).reshape(-1)
alpha_i = 1
beta = np.array([2, 2, 2, 2, 4, 4, 4, 4, 6, 6])
L = np.array([[2, -1, 0, -1, 0],
              [-1, 3, -1, -1, 0],
              [0, -1, 2, -1, 0],
              [-1, -1, -1, 4, -1],
              [0, 0, 0, -1, 1]])
A = np.array([[0, 1, 0, 1, 0],
              [1, 0, 1, 1, 0],
              [0, 1, 0, 1, 0],
              [1, 1, 1, 0, 1],
              [0, 0, 0, 1, 0]])
Aq = np.diag(A.flatten())
H = np.kron(L, np.eye(5)) + Aq

theta_bar_i = 9

tau_k_i = 70

doty = np.zeros((50, len(t)))
y_bar = np.zeros((50, len(t)))
nablaf = np.zeros((10, len(t)))
d = np.zeros((10, len(t)))
h = np.zeros((10, len(t)))
xi = np.zeros((10, len(t)))
dotv = np.zeros((10, len(t)))

for i in range(len(t)):
    y_bar[:, i] = y[:, i] - np.kron([[1]*5],x[:, i])
    doty[0:49:2, i] = -theta_bar_i * H @ y_bar[0:49:2, i]
    doty[1:50:2, i] = -theta_bar_i * H @ y_bar[1:50:2, i]

    nablaf[:, i] = [10 * y[0, i] + 2 * y[2, i] + 2 * y[4, i] - 2 * y[6, i] - 2 * y[8, i] - 4,
                    8 * y[1, i] - 2 * y[3, i] + 2 * y[5, i] - 2 * y[7, i] - 2 * y[9, i] - 2,
                    2 * y[10, i] + 10 * y[12, i] - 2 * y[14, i] + 2 * y[16, i] - 2 * y[18, i] + 2,
                    -2 * y[11, i] + 10 * y[13, i] + 2 * y[15, i] + 2 * y[17, i] - 2 * y[19, i] - 2,
                    2 * y[20, i] - 2 * y[22, i] + 10 * y[24, i] + 2 * y[26, i] - 2 * y[28, i] + 2,
                    2 * y[21, i] + 2 * y[23, i] + 10 * y[25, i] - 2 * y[27, i] - 2 * y[29, i] + 2,
                    -2 * y[30, i] + 2 * y[32, i] + 2 * y[34, i] + 10 * y[36, i] - 2 * y[38, i] - 4,
                    2 * y[31, i] + 2 * y[33, i] - 2 * y[35, i] + 10 * y[37, i] - 2 * y[39, i] + 4,
                    -2 * y[40, i] + 2 * y[42, i] + 2 * y[44, i] - 2 * y[46, i] + 10 * y[48, i] + 8,
                    -2 * y[41, i] - 2 * y[43, i] + 2 * y[45, i] + 2 * y[47, i] + 10 * y[49, i] + 8]

    y[:, i+1] = y[:, i] + dt * doty[:, i]
    d[:, i] = [2 * np.sin(i*dt), 2 * np.sin(i*dt), 2 * np.cos(i*dt), 2 * np.cos(i*dt), 4 * np.cos(2*i*dt), 4 * np.cos(2*i*dt),
               4 * np.sin(2*i*dt), 4 * np.sin(2*i*dt), 6 * np.sin(3*i*dt), 6 * np.sin(3*i*dt)]
    h[:, i] = v[:, i] + nablaf[:, i]
    xi[:, i] = h[:, i] / (np.abs(h[:, i]) + rho[:, i])
    dotv[:, i] = -tau_k_i * h[:, i] - beta * xi[:, i] + d[:, i]
    v[:, i+1] = v[:, i] + dt * dotv[:, i]
    x[:, i+1] = x[:, i] + dt * v[:, i+1]
    rho[:, i+1] = rho[:, i] + dt * (-alpha_i * rho[:, i])

t = np.arange(0, T+dt, dt)

plt.figure()
plt.plot(t, x[0], 'k', t, x[2], 'r', t, x[4], 'b', t, x[6], 'm', t, x[8], 'g', linewidth=1)
plt.xlabel('$t~\mathrm{(second)}$', fontsize=16)
plt.ylabel('$x_{i1}(t),$ for $i\in \{1,2,3,4,5\}$', fontsize=16)
plt.legend(['$x_{11}$', '$x_{21}$', '$x_{31}$', '$x_{41}$', '$x_{51}$'], fontsize=12)
plt.grid(True)

plt.figure()
plt.plot(t, x[1], 'k', t, x[3], 'r', t, x[5], 'b', t, x[7], 'm', t, x[9], 'g', linewidth=1)
plt.xlabel('$t~\mathrm{(second)}$', fontsize=16)
plt.ylabel('$x_{i2}(t),$ for $i\in \{1,2,3,4,5\}$', fontsize=16)
plt.legend(['$x_{12}$', '$x_{22}$', '$x_{32}$', '$x_{42}$', '$x_{52}$'], fontsize=12)
plt.grid(True)

# plt.figure()
# plt.plot(t, v.T, linewidth=1)
# plt.xlabel('$t~\mathrm{(second)}$', fontsize=16)
# plt.ylabel('$v_{ij}(t),$ for $i\in \{1,2,3,4,5\},~j\in \{1,2\}$', fontsize=16)
# plt.grid(True)
# plt.show()
