# Build the LP model
library(lpSolve)
# chance constained LP for Petorca Province Hypothetical Case
# Users: Agriculture, Domestic, Industry, Mining, InStream
prices <- c(50,100,51,51,50);
#
# constraint matrix
constraint <- array(0,dim=c(6,5));
# manual build
constraint[1,]  <- c(1,1,1,1,1)  # total delivery targets less than supply
constraint[2,]  <- c(1,0,0,0,0)  # Agriculture max use
constraint[3,]  <- c(0,1,0,0,0)  # Domestic max use
constraint[4,]  <- c(0,0,1,0,0)  # Industry max use
constraint[5,]  <- c(0,0,0,1,0)  # Mining max use
constraint[6,]  <- c(0,0,0,0,1)  # In-stream max use
#

#
rhs <- numeric(0)
#rhs <- c(200,160,20,10,4,6)  # Constraint values (50% reliability)
rhs <- c(53,160,20,10,4,6)  # Constraint values (90% reliability)
#
direction <- character(0)
for (i in 1:6){
  direction[i] <- "<="
}
print(prices)
print(cbind(constraint,direction,rhs))
# #
# # send to the LP solver
# #
prod.sol <- lp("max", prices, constraint, direction, rhs, compute.sens = TRUE)
# #accessing to R output
print(paste("Objective Value : ",prod.sol$objval))
for (i in 1:5){
print(paste("Decision [",i,"] = ",prod.sol$solution[i]))
}

