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
obj.fun <- c(0,.000513,0.00083)
# Define the constraint set
constr <- matrix(c(2,1,10,1,1,1,1,0,0,0,1,0,0,0,1), ncol = 3, byrow=TRUE)
constr.dir <- c("<=", ">=", "<=", "<=", "<=") 
rhs <- c(25, 20, 8, 15, 12)
######################################
# Solve the LP
wastewater.sol <- lp("min", obj.fun, constr, constr.dir, rhs, compute.sens = TRUE)
######################################
# Generate meaningful output
# Get some constants to make readable output
HowManyDecision <- length(wastewater.sol$solution)
message("Annual Operation Cost = $",wastewater.sol$objval) #objective function value 
for (i in 1:HowManyDecision) {
  message("Flow Through Plant ",i," = ",wastewater.sol$solution[i])
}
#######################################