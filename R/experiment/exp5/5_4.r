X <- c(-0.7, -5.6, 2, 2.8, 0.7, 3.5, 4, 5.8, 7.1, -0.5, 2.5, -1.6, 1.7, 3, 0.4, 4.5, 4.6, 2.5, 6, -1.4)
Y <- c(3.7, 6.5, 5, 5.2, 0.8, 0.2, 0.6, 3.4, 6.6, -1.1, 6, 3.8, 2, 1.6, 2, 2.2, 1.2, 3.1, 1.7, -2)
shapiro.test(X)
shapiro.test(Y)
ks.test(X, "pf", 2, 5)
ks.test(Y, "pf", 2, 5)
chisq.test(abs(X), correct = FALSE)
chisq.test(abs(Y))

t.test(X, Y, var.equal = TRUE, alternative = "less")
t.test(X, Y, var.equal = FALSE, alternative = "less")
t.test(X - Y, alternative = "less")

var.test(X, Y)
