f <- function(x) {
    n <- length(x)
    m <- mean(x)
    s <- sd(x)
    phi <- (n * sum(((x - m) / s)^3)) / ((n - 1) * (n - 2))
    phi
}

x <- rnorm(100)
f(x)
describe.by(x)
