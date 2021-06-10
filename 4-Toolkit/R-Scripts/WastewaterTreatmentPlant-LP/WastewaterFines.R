# Wastewater Treatment Plant Allocation
#####################################
# R script set-up
# deallocate the workspace
rm(list=ls())
# prototype function
MyCost <- function(x1,x2,x3){
  price <- c(0,4.3863e5,8.316e2)
  MyCost <- price[1]*x1+price[2]*x2+price[3]*x3
  return(MyCost)
}
MyLoad <- function(x1,x2,x3){
  price <- c(1.512e8,7.56e7,7.56e8)
  MyLoad <- price[1]*x1+price[2]*x2+price[3]*x3
  return(MyLoad)
}
# load the linear programming library
library(lpSolve)
#####################################
# LP Set-up
# Define the Objective Function
obj.fun <- c(0,4.3863e5,8.316e2)
# Define the constraint set
constr <- matrix(c(1,1,1,1,0,0,0,1,0), ncol = 3, byrow=TRUE)
#constr <- matrix(c(1,1,1,1,0,0,0,1,0,2,1,10), ncol = 3, byrow=TRUE)
constr.dir <- c(">=", "<=", "<=") 
#constr.dir <- c(">=", "<=", "<=", "<=") 
rhs <- c(20, 8, 15)
#rhs <- c(20, 8, 15, 25)
######################################
# Solve the LP
wastewater.sol <- lp("min", obj.fun, constr, constr.dir, rhs, compute.sens = TRUE)
######################################
# Generate meaningful output
# Get some constants to make readable output
HowManyDecision <- length(wastewater.sol$solution)
message("Annual Operation Cost = $",wastewater.sol$objval*1000) #objective function value 
for (i in 1:HowManyDecision) {
  message("Flow In Pipeline ",i," = ",wastewater.sol$solution[i])
}
#######################################