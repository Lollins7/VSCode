clc;
close all;
clear;
T = 20;
dt = 0.001;
m = 2;
lip = 2;
L1 = 20;
bartheta = 1;
k_i = 1;
N = 5;
t = 0:dt:T;
% x(:, 1) = randi([-10 10],10,1)*0.5;
x(: ,1) = [2.5, -2.5, 0, 2, 4, 5, 0.5, -4, -3.5, -2.5];
y(:, 1) = kron(ones(5, 1), x(:, 1));
v(:, 1) = zeros(10, 1);
rho(:, 1) = rand(10, 1);
alpha_i = 1;
beta = [2; 2; 2; 2; 4; 4; 4; 4; 6; 6];
L = [2, -1, 0, -1, 0; ...
    -1, 3, -1, -1, 0; ...
    0, -1, 2, -1, 0; ...
    -1, -1, -1, 4, -1; ...
    0, 0, 0, -1, 1];
A = [0, 1, 0, 1, 0; ...
    1, 0, 1, 1, 0; ...
    0, 1, 0, 1, 0; ...
    1, 1, 1, 0, 1; ...
    0, 0, 0, 1, 0];
Aq = diag(A(:));
H = kron(L, eye(5)) + Aq;
Q = eye(size(H));
P = lyap(H', Q);

minlamq = min(eig(Q));
theta = 1 + (lip + 2 * N * norm(P) * lip)^2 / (4 * m * minlamq) + 2 * sqrt(N) * norm(P) * lip / minlamq;
F = [m, -(lip + 2 * N * norm(P) * lip) / 2; ...
    -(lip + 2 * N * norm(P) * lip) / 2, theta * minlamq - 2 * sqrt(N) * norm(P) * lip];

% theta_bar_i = theta * bartheta;
theta_bar_i = 9;

minlamf = min(eig(F));
tau = 1 + (1 + 2 * sqrt(N) * norm(P) + theta * L1)^2 / (4 * minlamf * k_i);
G = [minlamf, -(1 + 2 * sqrt(N) * norm(P) + theta * L1) / 2; ...
    -(1 + 2 * sqrt(N) * norm(P) + theta * L1) / 2, tau * k_i];
% tau_k_i = tau * k_i;
tau_k_i = 70;

for i = 1:T / dt
    y_bar(:, i) = y(:, i) - kron(ones(5, 1), x(:, i));
    doty(1:2:50, i) = -theta_bar_i * H * y_bar(1:2:50, i);
    doty(2:2:50, i) = -theta_bar_i * H * y_bar(2:2:50, i);

    nablaf(1, i) = 10 * y(1, i) + 2 * y(3, i) + 2 * y(5, i) - 2 * y(7, i) - 2 * y(9, i) - 4;
    nablaf(2, i) = 8 * y(2, i) - 2 * y(4, i) + 2 * y(6, i) - 2 * y(8, i) - 2 * y(10, i) - 2;
    nablaf(3, i) = 2 * y(11, i) + 10 * y(13, i) - 2 * y(15, i) + 2 * y(17, i) - 2 * y(19, i) + 2;
    nablaf(4, i) = -2 * y(12, i) + 10 * y(14, i) + 2 * y(16, i) + 2 * y(18, i) - 2 * y(20, i) - 2;
    nablaf(5, i) = 2 * y(21, i) - 2 * y(23, i) + 10 * y(25, i) + 2 * y(27, i) - 2 * y(29, i) + 2;
    nablaf(6, i) = 2 * y(22, i) + 2 * y(24, i) + 10 * y(26, i) - 2 * y(28, i) - 2 * y(30, i) + 2;
    nablaf(7, i) = -2 * y(31, i) + 2 * y(33, i) + 2 * y(35, i) + 10 * y(37, i) - 2 * y(39, i) - 4;
    nablaf(8, i) = 2 * y(32, i) + 2 * y(34, i) - 2 * y(36, i) + 10 * y(38, i) - 2 * y(40, i) + 4;
    nablaf(9, i) = -2 * y(41, i) + 2 * y(43, i) + 2 * y(45, i) - 2 * y(47, i) + 10 * y(49, i) + 8;
    nablaf(10, i) = -2 * y(42, i) - 2 * y(44, i) + 2 * y(46, i) + 2 * y(48, i) + 10 * y(50, i) + 8;

    y(1:2:50, i+1) = y(1:2:50, i) + dt * doty(1:2:50, i);
    y(2:2:50, i+1) = y(2:2:50, i) + dt * doty(2:2:50, i);
    d(:, i) = [2 * sin(i*dt), 2 * sin(i*dt), 2 * cos(i*dt), 2 * cos(i*dt), 4 * cos(2*i*dt), 4 * cos(2*i*dt), ...
        4 * sin(2*i*dt), 4 * sin(2*i*dt), 6 * sin(3*i*dt), 6 * sin(3*i*dt)];
    h(:, i) = v(:, i) + nablaf(:, i);
    xi(:, i) = h(:, i) ./ (abs(h(:, i)) + rho(:, i));
    dotv(:, i) = -tau_k_i * h(:, i) - beta .* xi(:, i) + d(:, i);
    v(:, i+1) = v(:, i) + dt * dotv(:, i);
    x(:, i+1) = x(:, i) + dt * v(:, i+1);
    rho(:, i+1) = rho(:, i) + dt * (-alpha_i * rho(:, i));
end


myfigure1 = figure;
plot(t, x(1, :), 'k', t, x(3, :), 'r', t, x(5, :), 'b', t, x(7, :), 'm', t, x(9, :), 'g', 'LineWidth', 1)
h1 = legend('$x_{11}$', '$x_{21}$', '$x_{31}$', '$x_{41}$', '$x_{51}$', 'FontSize', 12, 'Interpreter', 'latex');
set(h1, 'Interpreter', 'latex', 'Fontsize', 16)
xlabel('$t~\rm(second)$', 'Interpreter', 'latex', 'fontsize', 16)
ylabel('$x_{i1}(t),$ for $i\in \{1,2,3,4,5\}$', 'fontsize', 16, 'Interpreter', 'latex');
set(h1, 'Interpreter', 'latex', 'fontsize', 16, 'Location', 'EastOutside')
%set(gca,'Ytick',[-4:0.5:3])

myfigure2 = figure;
plot(t, x(2, :), 'k', t, x(4, :), 'r', t, x(6, :), 'b', t, x(8, :), 'm', t, x(10, :), 'g', 'LineWidth', 1)
h2 = legend('$x_{12}$', '$x_{22}$', '$x_{32}$', '$x_{42}$', '$x_{52}$');
set(h2, 'Interpreter', 'latex', 'Fontsize', 16)
xlabel('$t~\rm(second)$', 'Interpreter', 'latex', 'fontsize', 16)
ylabel('$x_{i2}(t),$ for $i\in \{1,2,3,4,5\}$', 'fontsize', 16, 'Interpreter', 'latex');
set(h2, 'Interpreter', 'latex', 'fontsize', 16, 'Location', 'EastOutside')

myfigure3 = figure;
plot(t, v, 'LineWidth', 1)
xlabel('$t~\rm(second)$', 'Interpreter', 'latex', 'fontsize', 16)
ylabel('$v_{ij}(t),$ for $i\in \{1,2,3,4,5\},~j\in \{1,2\}$', 'fontsize', 16, 'Interpreter', 'latex');

% myfigure4 = figure;
% subplot(2, 1, 1)
% plot(t, d(1, :), 'k', t, d_b(1, :), 'k:', t, d(3, :), 'r', t, d_b(3, :), 'r:', t, d(5, :), 'b', t, d_b(5, :), 'b:', t, d(7, :), 'm', t, d_b(7, :), 'm:', t, d(9, :), 'g', t, d_b(9, :), 'g:', 'LineWidth', 1)
% ylabel('$d_{m1}(t),~\hat{d}_{m1}(t)$', 'fontsize', 16, 'Interpreter', 'latex')
%
% subplot(2, 1, 2)
% plot(t, d(2, :), 'k', t, d_b(2, :), 'k:', t, d(4, :), 'r', t, d_b(4, :), 'r:', t, d(6, :), 'b', t, d_b(6, :), 'b:', t, d(8, :), 'm', t, d_b(8, :), 'm:', t, d(10, :), 'g', t, d_b(10, :), 'g:', 'LineWidth', 1)
% ylabel('$d_{m2}(t),~\hat{d}_{m2}(t)$', 'fontsize', 16, 'Interpreter', 'latex')
% xlabel('$t~\rm(second)$', 'Interpreter', 'latex', 'fontsize', 16)
% h1 = legend('$d_{m}(t)$', '$\hat{d}_{m}(t)$');
% set(h1, 'Interpreter', 'latex', 'fontsize', 16, 'Location', 'best', 'Orientation', 'horizontal')
