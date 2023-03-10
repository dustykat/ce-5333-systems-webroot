# explorations of chance constraints
# Build the LP model
library(lpSolve)
# chance constained LP
prices <- c(100,40,40.001);
#
# constraint matrix
constraint <- array(0,dim=c(7,3));
# manual build
constraint[1,]  <- c(1,1,1)
constraint[2,]  <- c(1,0,0)
constraint[3,]  <- c(0,1,0)
constraint[4,]  <- c(0,0,1)
constraint[5,]  <- c(1,0,0)
constraint[6,]  <- c(0,1,0)
constraint[7,]  <- c(0,0,1)

#
rhs <- numeric(0)
rhs <- c(6,2,3,5,1,1,1)
#
direction <- character(0)
for (i in 1:4){
  direction[i] <- "<="
}
for (i in 5:7){
  direction[i] <- ">="
}
print(prices)
print(cbind(constraint,direction,rhs))
# #
# # send to the LP solver
# #
prod.sol <- lp("max", prices, constraint, direction, rhs, compute.sens = TRUE)
# #accessing to R output
print(paste("Objective Value : ",prod.sol$objval))
for (i in 1:3){
  print(paste("Decision [",i,"] = ",prod.sol$solution[i]))
}
# prod.sol$duals #includes duals of constraints and reduced costs of variables
# #sensibility analysis results
# prod.sol$duals.from
# prod.sol$duals.to
# prod.sol$sens.coef.from
# prod.sol$sens.coef.to
# # test alternate solutions