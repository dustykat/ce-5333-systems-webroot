# Build the LP model
library(lpSolve)
# read in the influence matrix
#zz <- read.csv("influence-table-output.txt",header=FALSE)

probabilities <- c(1,1,1,0.2,0.2,0.2,0.6,0.6,0.6,0.2,0.2,0.2);
unit_cost     <- c(100,50,49,-250,-75,-79,-250,-75,-79,-250,-75,-79);
prices <- probabilities*unit_cost
#
# constraint matrix
constraint <- array(0,dim=c(21,12));
# manual build
constraint[1,]  <- c(1,1,1,-1,-1,-1,0,0,0,0,0,0)
constraint[2,]  <- c(1,1,1,0,0,0,-1,-1,-1,0,0,0)
constraint[3,]  <- c(1,1,1,0,0,0,0,0,0,-1,-1,-1)
constraint[4,]  <- c(1,0,0,-1,0,0,0,0,0,0,0,0)
constraint[5,]  <- c(0,1,0,0,-1,0,0,0,0,0,0,0)
constraint[6,]  <- c(0,0,1,0,0,-1,0,0,0,0,0,0)
constraint[7,] <- c(1,0,0,0,0,0,-1,0,0,0,0,0)
constraint[8,] <- c(0,1,0,0,0,0,0,-1,0,0,0,0)
constraint[9,] <- c(0,0,1,0,0,0,0,0,-1,0,0,0)
constraint[10,] <- c(1,0,0,0,0,0,0,0,0,-1,0,0)
constraint[11,] <- c(0,1,0,0,0,0,0,0,0,0,-1,0)
constraint[12,] <- c(0,0,1,0,0,0,0,0,0,0,0,-1)
constraint[13,]  <- c(1,0,0,-1,0,0,0,0,0,0,0,0)
constraint[14,]  <- c(0,1,0,0,-1,0,0,0,0,0,0,0)
constraint[15,]  <- c(0,0,1,0,0,-1,0,0,0,0,0,0)
constraint[16,] <- c(1,0,0,0,0,0,-1,0,0,0,0,0)
constraint[17,] <- c(0,1,0,0,0,0,0,-1,0,0,0,0)
constraint[18,] <- c(0,0,1,0,0,0,0,0,-1,0,0,0)
constraint[19,] <- c(1,0,0,0,0,0,0,0,0,-1,0,0)
constraint[20,] <- c(0,1,0,0,0,0,0,0,0,0,-1,0)
constraint[21,] <- c(0,0,1,0,0,0,0,0,0,0,0,-1)
#
rhs <- numeric(0)
rhs <- c(4,10,17,2,3,5,2,3,5,2,3,5,1,1,1,1,1,1,1,1,1)
#
direction <- character(0)
for (i in 1:3){
  direction[i] <- "<="
}
for (i in 4:12){
  direction[i] <- "<="
}
for (i in 13:21){
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
for (i in 1:12){
print(paste("Decision [",i,"] = ",prod.sol$solution[i]))
}
# prod.sol$duals #includes duals of constraints and reduced costs of variables
# #sensibility analysis results
# prod.sol$duals.from
# prod.sol$duals.to
# prod.sol$sens.coef.from
# prod.sol$sens.coef.to
# # test alternate solutions
