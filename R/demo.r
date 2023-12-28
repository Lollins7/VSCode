lamp<-data.frame(
  X=c(1600, 1610, 1650, 1680, 1700, 1700, 1780, 1500, 1640,
      1400, 1700, 1750, 1640, 1550, 1600, 1620, 1640, 1600,
      1740, 1800, 1510, 1520, 1530, 1570, 1640, 1600),
  A=factor(c(rep(1,7),rep(2,5), rep(3,8), rep(4,6)))
)

lamp.aov<-aov(X ~ A, data=lamp)

summary(lamp.aov)

tab <- summary(lamp.aov)

length(tab[[1]])


