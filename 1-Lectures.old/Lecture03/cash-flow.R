# cash flow calculations
discount_rate <- 0.03 # 3% interest rate
payments <- rep(100,10)
present_value <- numeric(0)
present_value <- 0
for (i in 1:10){ #find present value of the i-th year payment
  present_value[i] <- payments[i]*(1+discount_rate)^(-i)
}
#add up all the present values
message("Present Worth of 10 annual payments of $100 @ 3% interest is $",sum(present_value))