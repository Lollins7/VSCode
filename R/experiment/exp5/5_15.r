x <- c(13.32, 13.06, 14.02, 11.86, 13.58, 13.77, 13.51, 14.42, 14.44, 15.43)
binom.test(sum(x > 14.6), length(x), al = "l")
wilcox.test(x, mu = 14.6, alternative = "l", exact = FALSE, correct = FALSE, conf.int = TRUE)
