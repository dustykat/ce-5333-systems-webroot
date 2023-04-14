# Wastewater Treatment Plant Allocation
#####################################
# R script set-up
# deallocate the workspace
rm(list=ls())
# load the linear programming library
library(lpSolve)
#####################################
# LP Set-up
# Define the Objective Function
obj.fun <- c(3.88e6,2.88e6,833)
# Define the constraint set
constr <- matrix(c(2,1,10,  1,0,0,  0,1,0, 1,1,1), ncol = 3, byrow=TRUE)
constr.dir <- c("<=", "<=", "<=", ">=") 
rhs <- c(20, 8, 15, 20)
######################################
# Solve the LP
wastewater.sol <- lp("min", obj.fun, constr, constr.dir, rhs, compute.sens = TRUE)
######################################
# Generate meaningful output
# Get some constants to make readable output
HowManyDecision <- length(wastewater.sol$solution)
message("Annual Operation Cost = $",wastewater.sol$objval) #objective function value 
for (i in 1:HowManyDecision) {
  message("Flow In Pipeline ",i," = ",wastewater.sol$solution[i])
}
#######################################