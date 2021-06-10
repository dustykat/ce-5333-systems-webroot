# Construction Management Model 
#####################################
# R script set-up
# deallocate the workspace
rm(list=ls())
# load the linear programming library
library(lpSolve)
#####################################
# LP Set-up
# Define the Objective Function
obj.fun <- c(394, 1110)
# Define the constraint set
constr <- matrix(c(200, 1000, 200, 0, 0, 1000, 1, 1), ncol = 2, byrow=TRUE)
constr.dir <- c("<=", ">=", ">=", "<=") 
rhs <- c(10000, 1600, 3000, 12)
######################################
# Solve the LP
construction.sol <- lp("min", obj.fun, constr, constr.dir, rhs, compute.sens = TRUE)
######################################
# Generate meaningful output
# Get some constants to make readable output
HowManyDecision <- length(construction.sol$solution)
message("Daily Operation Cost = $",construction.sol$objval) #objective function value 
for (i in 1:HowManyDecision) {
  message("Workers Assigned to Backhoe ",i," = ",construction.sol$solution[i])
}
#######################################
