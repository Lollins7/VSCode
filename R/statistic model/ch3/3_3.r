a <- read.table("data//3_1.txt")
a <- as.numeric(unlist(a))
stem(a)
boxplot(a, col = "#a00cb6")
fivenum(a)
