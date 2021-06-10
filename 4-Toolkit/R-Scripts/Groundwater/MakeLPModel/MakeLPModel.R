# Build the LP model
library(lpSolve)
# read in the influence matrix
zz <- read.csv("influence-table-output.txt",header=FALSE)
# build the cost vector
xdist <- c(1,3,5,7,9)
ydist <- c(1,3,5,7,9)
x0 <- 5
y0 <- 3
cost <- numeric(0)
icell <- 0
for (j in 5:1){
  for( i in 5:1){
    icell <- icell+1
    distance <- sqrt((xdist[i]-x0)^2 + (ydist[j]-y0)^2)
    cost[icell] <- 1.0 + 0.5*distance
#    print(paste(icell," dist= ",distance," row= ",i," col=",j,"cost = ",cost[icell]))
  }
}
# build the demand constraint
demand <- rep(1,25)
# build the constraint values
crhs <- c(0.00,0.00,0.00,0.00,0.00,
          0.00,0.00,0.00,0.00,0.00,
          0.00,0.00,0.00,0.00,0.00,
          6.27,6.27,6.27,6.27,6.27,
          2.15,2.15,2.15,2.15,2.15,
          7.00,
          0.00,0.00,0.00,0.00,0.00)
# 
# build the LP constraint matrix
#
cmatrix <- matrix(0,nrow=31,ncol=25)
for (i in 1:25){
  for (j in 1:25){
    cmatrix[i,j] <- zz[i,j]
  }
}
cmatrix[26,] <- demand
# force Zeros in cells 21-25
cmatrix[27,] <- c(rep(0,20),1,rep(0,4))
cmatrix[28,] <- c(rep(0,21),1,rep(0,3))
cmatrix[29,] <- c(rep(0,22),1,rep(0,2))
cmatrix[30,] <- c(rep(0,23),1,rep(0,1))
cmatrix[31,] <- c(rep(0,24),1         )
#
# build the LP constraint directions
#
cdirection <- character(0)
for (i in 1:15){
  cdirection[i] <- ">="
}
for (i in 16:25){
  cdirection[i] <- "<="
}
for (i in 26:31){
  cdirection[i] <- "="
}
#
# send to the LP solver
#
prod.sol <- lp("min", cost, cmatrix, cdirection, crhs, compute.sens = TRUE)
#accessing to R output
message("Objective Value = : ", prod.sol$objval)
decisionMatrix <- matrix(0,nrow=5,ncol=5)
index <- 0
for (irow in 1:5){
  for (jcol in 1:5){
    index <- index+1
    decisionMatrix[irow,jcol] <- prod.sol$solution[index]
  }
}
message("Decision (Pumping) Matrix = : ")
print(decisionMatrix, byrow=TRUE)
message("Constraint Check = : ")
constCheck <- cmatrix%*%prod.sol$solution
print(cbind(constCheck,cdirection,crhs))
prod.sol$duals #includes duals of constraints and reduced costs of variables
#sensibility analysis results
prod.sol$duals.from
prod.sol$duals.to
prod.sol$sens.coef.from
prod.sol$sens.coef.to
# test alternate solutions
value <- t(cost)%*%c(rep(0,15),1.160381,1.797931 ,1.627169 ,1.797931,1.160381, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000)
message("Alternate Solution Objective Value = : ",value)
decisionVector <- c(rep(0,15),1.160381,1.797931 ,1.627169 ,1.797931,1.160381, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000)
index <- 0
for (irow in 1:5){
  for (jcol in 1:5){
    index <- index+1
    decisionMatrix[irow,jcol] <- decisionVector[index]
  }
}
print(decisionMatrix, byrow=TRUE)
constCheck <- cmatrix%*%c(rep(0,15),1.160381,1.797931 ,1.627169 ,1.797931,1.160381, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000)
message("Constraint Equation Values = :")
print(cbind(constCheck,cdirection,crhs))

# test alternate solutions
value <- t(cost)%*%c(rep(0,15),0.5801905,2.414519 ,1.627169 ,1.797931,0.5801905, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000)
message("Alternate Solution Objective Value = : ",value)
decisionVector <- c(rep(0,15),0.5801905,2.414519 ,1.627169 ,1.797931,0.5801905, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000)
index <- 0
for (irow in 1:5){
  for (jcol in 1:5){
    index <- index+1
    decisionMatrix[irow,jcol] <- decisionVector[index]
  }
}
print(decisionMatrix, byrow=TRUE)
constCheck <- cmatrix%*%c(rep(0,15),0.5801905,2.414519 ,1.627169 ,1.797931,0.5801905, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000)
message("Constraint Equation Values = :")
print(cbind(constCheck,cdirection,crhs))
# value <- t(cost)%*%c(rep(0,15),0.5801905,2.414519 ,1.627169 ,1.797931,0.5801905, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000)
# print(value)
# # check constrainst for alternates
# check <- cmatrix%*%c(rep(0,15),1.160381,2.414519 ,1.627169 ,1.797931,0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000)
# print(check)
# check <- cmatrix%*%c(rep(0,15),0.5801905,2.414519 ,1.627169 ,1.797931,0.5801905, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000)
# print(check)