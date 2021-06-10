# cash flow calculations for ES3
rm(list=ls())
discount_rate <- 0.05 # 3% interest rate
# option A
# compute present values of expenses first 10 years
initial_costA <- 10000
operationsA <- rep(2000,10)
salvageA <- 1000
### compute the PV of the operations cost
present_value <- numeric(0)
present_value <- 0
for (i in 1:10){ #find present value of the i-th year payment
  present_value[i] <- operationsA[i]*(1+discount_rate)^(-i)
}
operationsAPV <- sum(present_value)
### compute the PV of the salvage payment
salvageAPV <- salvageA*(1+discount_rate)^(-10)
#print(cbind(initial_costA,operationsAPV,salvageAPV))
# now compute the PV for the second 10 years
presentValueA1 <- initial_costA+operationsAPV+salvageAPV
presentValueA2 <- presentValueA1*(1+discount_rate)^(-10)
presentValueA <- presentValueA1+presentValueA2
message("Present Value A = $",presentValueA)
########## Alternative B #################
initial_costB <- 25000
operationsB <- rep(1500,20)
salvageB <- 5000
### compute the PV of the operations cost
present_value <- numeric(0)
present_value <- 0
for (i in 1:20){ #find present value of the i-th year payment
  present_value[i] <- operationsB[i]*(1+discount_rate)^(-i)
}
operationsBPV <- sum(present_value)
### compute the PV of the salvage payment
salvageBPV <- salvageB*(1+discount_rate)^(-20)
#print(cbind(initial_costB,operationsBPV,salvageBPV))
presentValueB <- initial_costB+operationsBPV+salvageBPV
message("Present Value B = $",presentValueB)
# now convert both to annual costs
### compute the PV of the operations cost
present_valueA <- numeric(0)
present_valueA <- 0
### compute the PV of the operations cost
present_valueB <- numeric(0)
present_valueB <- 0
## read in guess for annual cost
  avA <- readline(prompt="Enter annual cost for alternative A: ")
  avA <- as.numeric(avA)
  avB <- readline(prompt="Enter annual cost for alternative B: ")
  avB <- as.numeric(avB)
#avA <- 3374.55
#avB <- 3657.28
annualA <- rep(avA,20)
annualB <- rep(avB,20)
for (i in 1:20){ #find present value of the i-th year payment
  present_valueA[i] <- annualA[i]*(1+discount_rate)^(-i)
  present_valueB[i] <- annualB[i]*(1+discount_rate)^(-i)
}
message("annual cost A = $",avA," PVA = $",sum(present_valueA)," PValue A = $",presentValueA)
message("annual cost B = $",avB," PVB = $",sum(present_valueB)," PValue B = $",presentValueB)

