circle <- function(n) {
    if (n <= 0) {
        print("要求输入一个正整数")
    } else {
        while (n != 1) {
            if (n %% 2 == 0) {
                n <- n / 2
            } else {
                n <- 3 * n + 1
            }
        }
    }
    print("定理成立")
}
circle(3)
