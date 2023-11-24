X<-c(5.1,3.5,7.1,6.2,8.8,7.8,4.5,5.6,8,6.4)
Y<-c(1907,1287,2700,2373,3260,3000,1947,2273,3113,2493)
plot(X,Y)

intellect<-data.frame(X,Y)
lm.sol<-lm(Y~X,data=intellect)
summary(lm.sol)

new<-data.frame(X=7)
lm.pred<-predict(lm.sol,new,interval="prediction",level=0.95)
lm.pred

