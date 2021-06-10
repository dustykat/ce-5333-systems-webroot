# build graphics
q <- c(4,10,17)
p <- c(0.2,0.6,0.2)
plot(q,p,ylim=c(0,1),type="s")
qq<- c(4,4,4,10,10,17,17,17)
pp<- c(0,0.2,0,0.6,0,0,0.2,0)
plot(qq,pp,type="l",lwd=3,xlab="Streamflow",ylab="Probability")
boxplot(q)
