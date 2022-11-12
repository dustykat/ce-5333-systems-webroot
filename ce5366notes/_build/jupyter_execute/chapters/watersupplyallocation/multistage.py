#!/usr/bin/env python
# coding: utf-8

# # Allocation under Uncertainty
# 
# Introduction of uncertainty into an allocation problem creates a stochastic programming situation. There are a variety of methods to address stochastic programming including:
# 
# - Stochastic dynamic programming
# - Stochastic linear programming
# - Multi-Stage Linear Programming
# - Chance Constraint Programming
# 
# the two examples below consider a case where the problem is linear enough for a linear programming solution. 
# 
# Using linear programming (LP) directly for stochastic problems results in a large increase in the number of variables and constraints to account for alternative scenarios or in the use of chance constraints. Each of these two approaches are explored below – first two-stage linear programming by means of a simple example, then the same example is repeated using chance constraints.

# ## Two-Stage Linear Programming Example
# 
# A water master for a region can divert water from an unregulated stream to three consumers: a municipality, an industrial concern, and an agricultural concern. A schematic of the system is shown in {numref}`diversionsketch`.
# 
# ```{figure} diversionsketch.png
# ---
# width: 400px
# name: diversionsketch
# ---
# Schematic of water supply allocation problem
# ```
# 
# The industrial and agricultural concern are expanding and would like to know how much water they can expect. If the water supply is insufficient, the expansion plans will be curtailed.
# 
# The unregulated streamflow is a random variable, and the goal of the water master is to maximize benefit to the water supply authority.
# 
# Let $T_i$ represent the contracted quantity of water the supplier will deliver to each user $i$.
# If the water is delivered, the resulting net benefits to the local economy are estimated to be $NB_i$.
# However, if the water is not delivered, water must be obtained from an alternate source, or demand must be curtailed by rationing of the municipal users, reduced production by industrial users, or reduced irrigation by the agricultural users.
# Such deficits reduce the net benefits to user $i$ by a cost $C_i$ per unit of water not supplied.
# Each user can provide the water master with an estimate of the maximum amount of water they can use, $T^{max}_i$.
# 
# $Q$, the total water available, is a random variable described by some probability distribution.  
# The water master's goal is to maximize the expected net benefit to the region by allocating water to the three users.

# ### Linear Programming Model Framework
# Let the deficit for a delivery be denoted by the variable $D_{i,j}$, where the $i$ subscript refers to a particular user, and the $j$ subscript refers to the particular random supply scenario.
# 
# The water masters allocation problem is then to maximize expected benefit.  
# Recall an expected cost (or benefit) is the product of the probability of an outcome and the value (cost) of the outcome.
# 
# In this example the benefits of the deliveries is assured (probability = 1), but the costs of the deficits are stochastic, hence the benefit function is 
# 
# $$
# \begin{equation}
# NB = NB_1 \cdot T_1 + NB_2 \cdot T_2 + NB_3 \cdot T_3 - E(C_1 \cdot D_{1,Q} + C_2 \cdot D_{2,Q} + C_3 \cdot D_{3,Q})
# \end{equation}
# $$
# 
# The constraints to be applied are
# 
# $$
# \begin{equation}
#  T_1 + T_2 + T_3 - [D_{1,Q} -D_{2,Q} -D_{3,Q}] \le Q
# \end{equation}
# $$
# 
# and
# 
# $$
# \begin{equation}
# 0 \le T_i  - D_{i,Q} \le T^{max}_i
# \end{equation}
# $$
# 

# ### Approximating the Random Variable
# 
# To approximate the value of the expectation, we can approximate the distribution of $Q$ with a discrete distribution as in {numref}`flowprob`.  For a continuous distribution, some kind of discretization will be required to keep the LP manageable.
# 
# ```{figure} flowprob.png
# ---
# width: 400px
# name: flowprob
# ---
# Streamflow probability distribution
# ```
# 
# The approximation allows the estimation of the expected cost (of failed delivery) to be manifest in the objective function, and the supply availability in the constraint set.  The model in this instance (3 customers, 3 possible supply rates) has a total of 12 decision variables; the three contracted deliveries and nine deficits (from the 3 possible supply rates).
# 
# The cost function becomes:
# 
# $$
# \begin{equation}
# \begin{matrix}
# NB = & NB_1\cdot T_1 + NB_2 \cdot T_2 + NB_3 \cdot T_3   & - p_1(C_1 \cdot D_{1,1} + C_2 \cdot D_{2,1} + C_3 \cdot D_{3,1}) \\
# ~ & ~ & - p_2(C_1 \cdot D_{1,2} + C_2 \cdot D_{2,2} + C_3 \cdot D_{3,2}) \\
# ~ & ~ & - p_3(C_1 \cdot D_{1,3} + C_2 \cdot D_{2,3} + C_3 \cdot D_{3,3}) \\
# \end{matrix}
# \end{equation}
# $$
# 
# The constraint set becomes:
# 
# $$
# \begin{equation}
# \begin{matrix}
# T_1 + T_2 + T_3 & -D_{1,1} - D_{2,1} - D_{3,1} &  &  & \le & q_1 \\
# T_1 + T_2 + T_3 &  & -D_{1,2} - D_{2,2} - D_{3,2} &  & \le & q_2 \\
# T_1 + T_2 + T_3 &  &  & -D_{1,3} - D_{2,3} - D_{3,3} & \le & q_3 \\
# \hline
# T_1 ~~~~ ~~~~ & -D_{1,1} ~~~~ ~~~~ &  &  & \le & T^{max}_1 \\
# ~~~~ T_2 ~~~~ & ~~~~ - D_{2,1} ~~~~ &  & & \le & T^{max}_2 \\
# ~~~~ ~~~~ T_3 & ~~~~ ~~~~  - D_{3,1} & & & \le & T^{max}_3 \\
# \hline
# T_1 ~~~~ ~~~~ &  & -D_{1,2} ~~~~ ~~~~ &  & \le & T^{max}_1\\
# ~~~~ T_2 ~~~~ &  & ~~~~ - D_{2,2} ~~~~ &  & \le & T^{max}_2 \\
# ~~~~ ~~~~ T_3 &  & ~~~~ ~~~~ - D_{3,2} &  & \le & T^{max}_3 \\
# \hline
# T_1 ~~~~ ~~~~&  &  & -D_{1,3} ~~~~ ~~~~ & \le & T^{max}_1 \\
# ~~~~ T_2 ~~~~ &  &  & ~~~~ -D_{2,3} ~~~~ & \le & T^{max}_2 \\
# ~~~~ ~~~~ T_3 &  &  & ~~~~ ~~~~ - D_{3,3} & \le & T^{max}_3 \\
# \hline
# T_1 ~~~~ ~~~~ & -D_{1,1} ~~~~ ~~~~ &  &  & \ge & 0 \\
# ~~~~ T_2 ~~~~ & ~~~~ - D_{2,1} ~~~~ &  &  & \ge & 0 \\
# ~~~~ ~~~~ T_3 & ~~~~ ~~~~  - D_{3,1} &  &  & \ge & 0 \\
# \hline
# T_1 ~~~~ ~~~~ &  & -D_{1,2} ~~~~ ~~~~ &  & \ge & 0\\
# ~~~~ T_2 ~~~~ &  & ~~~~ - D_{2,2} ~~~~ &  & \ge & 0 \\
# ~~~~ ~~~~ T_3 &  & ~~~~ ~~~~ - D_{3,2} &  & \ge & 0 \\
# \hline
# T_1 ~~~~ ~~~~&  &  & -D_{1,3} ~~~~ ~~~~ & \ge & 0 \\
# ~~~~ T_2 ~~~~ &  &  & ~~~~ -D_{2,3} ~~~~ & \ge & 0 \\
# ~~~~ ~~~~ T_3 &  &  & ~~~~ ~~~~ - D_{3,3} & \ge & 0 \\
# \\
# \end{matrix}
# \end{equation}
# $$
# 
# The solution to this Linear Program would provide the water master with an optimal allocation of contracted (promised delivery) as well as an estimate (implicit in the solution) of the resource allocations to make when supply is insufficient.

# ### Technological and Probability Values
# 
# Assume for this example that the benefit and cost information for the three uses and the maximum value that each user can assimilate is tabulated below
# 
# |User|Index|$T^{max}_i$|$NB_i$|$C_i$|
# |:---|---:|---:|---:|---:|
# |Municipal   |1|2|100|250|
# |Industrial  |2|3| 50| 75|
# |Agricultural|3|5| 30| 60|
# 
# Similarily a tabulation of the streamflow probability distribution for the region.
# 
# |Flow Index, j | $q_j$ | $p_j$ |
# |:---|---:|---:|
# |1 | 4 | 0.20 |
# |2 | 10 | 0.60 |
# |3 | 17 | 0.20 |
# 
# The values in these two tables are inserted into their representative locations in the linear program structure (cost function and constraint set). Once these values are supplied, then we have the necessary set-up for a Linear Program and can apply our tools to its solution.
# So the linear program to be solved is depicted in {numref}`linearP`
# 
# ```{figure} linearP.png
# ---
# width: 600px
# name: linearP
# ---
# Linear Program Structure for Water Supply Allocation Problem
# ```

# ### Linear Programming Model Solution
# 
# To solve the LP we need to translate the framework from {numref}`linearP` into a structure for our solver tool to process.  
# 
# The process to solve the problem  is to build the cost function weights, then the constraint matrix coefficients, then the right hand side, and finally the sense of the constraints.  Once these are built, the objects can be sent to the program for a solution.
# 
# For this example, the cost function unit values are hand-entered and the probabilities are explicitly supplied in the coeffficients.
# The coefficients for the cost function are created element-by-element, the result is what will be sent to the LP solver algorithm.
# 
# The constraint matrix is constructed row-wise, again by hand.  
# The right-hand-side matrix is also hand constructed.
# The sense of the inequalities is constructed semi-automatically by taking advantage of how the tableau is structured.

# In[1]:


from scipy.optimize import linprog
ct1 = 100
ct2 = 50
ct3 = 30
cd11 = -0.2*250
cd21 = -0.2*75
cd31 = -0.2*60
cd12 = -0.6*250
cd22 = -0.6*75
cd32 = -0.6*60
cd13 = -0.2*250
cd23 = -0.2*75
cd33 = -0.2*60
obj = [-ct1,-ct2,-ct3,-cd11,-cd21,-cd31,-cd12,-cd22,-cd32,-cd13,-cd23,-cd33] # sign change to coerce maximization to minimization, multiply result by -1 to restore to orginal state
lhs_ineq = [[  1, 1, 1,-1,-1,-1, 0, 0, 0, 0, 0, 0],  # lhs row 1
            [  1, 1, 1, 0, 0, 0,-1,-1,-1, 0, 0, 0],  # lhs row 2
            [  1, 1, 1, 0, 0, 0, 0, 0, 0,-1,-1,-1],  # lhs row 3
            [  1, 0, 0,-1, 0, 0, 0, 0, 0, 0, 0, 0],  # lhs row 4 sign change to get >= status
            [  0, 1, 0, 0,-1, 0, 0, 0, 0, 0, 0, 0],  # lhs row 5
            [  0, 0, 1, 0, 0,-1, 0, 0, 0, 0, 0, 0],  # lhs row 6
            [  1, 0, 0, 0, 0, 0,-1, 0, 0, 0, 0, 0],  # lhs row 7
            [  0, 1, 0, 0, 0, 0, 0,-1, 0, 0, 0, 0],  # lhs row 8
            [  0, 0, 1, 0, 0, 0, 0, 0,-1, 0, 0, 0],  # lhs row 9
            [  1, 0, 0, 0, 0, 0, 0, 0, 0,-1, 0, 0],  # lhs row 10
            [  0, 1, 0, 0, 0, 0, 0, 0, 0, 0,-1, 0],  # lhs row 11
            [  0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0,-1],  # lhs row 12
            [ -1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],  # lhs row 13
            [  0,-1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],  # lhs row 14
            [  0, 0,-1, 0, 0, 1, 0, 0, 0, 0, 0, 0],  # lhs row 15
            [ -1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],  # lhs row 16
            [  0,-1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],  # lhs row 17
            [  0, 0,-1, 0, 0, 0, 0, 0, 1, 0, 0, 0],  # lhs row 18
            [ -1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],  # lhs row 19
            [  0,-1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],  # lhs row 20
            [  0, 0,-1, 0, 0, 0, 0, 0, 0, 0, 0, 1] ] # lhs row 21
rhs_ineq = [4,
            10,
            14,
            2,
            3,
            5,
            2,
            3,
            5,
            2,
            3,
            5,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0]


# Finally all the elements are sent to the algorithm which builds and solves the example problem.
# <!--![](linearP.png)-->

# In[2]:


opt = linprog(c=obj, A_ub=lhs_ineq, b_ub=rhs_ineq,method="revised simplex")
opt


# Once the script run, the output then needs to be interpreted. Observe that the output object is a dictionary-type object, which we access from the element keys.  The objective value is converted back to the maximization case by multiplying by -1.
# 
# :::{note}
# The sense of optimization in the base `scipy.optimize` package is always **minimize** the inequalities are always **<=**.  By use of multiplication of -1 in the appropriate parts of the problem we convert it to a maximization problem.
# :::

# In[3]:


objval=-1*opt['fun']
policyvector = opt['x']

print("Objective Function Value :",objval)
for i in range(len(policyvector)):
    print("x_",i+1," :",policyvector[i])


# The optimal solution is to contract deliveries to each user at the full amount they request.
# The expected net benefit is $425$ benefit units.
# There is a 20\% chance that users 2 and 3 will have deficits and the water master will incur costs.
# There is an 80\% chance that all users will get their contracted water, and a 20\% chance that there will be excess water available.
# 
# If the system had storage the 20\% excess cases could be used to help satisfy the one case when the system does not have enough input.
# 
# A useful collateral result is that when the water input is too small to satisfy all the contracts, the solution also suggests how to make the allocations in the limited case -- the municipal users are supplied their full amount, industry receives the remainder of the available water (and has a deficit of 1 unit), and agriculture is denied its entire request.  
# 
# The allocations would change if the unit benefits reflected the value of the water differently to the three users and/or the deficit costs changed.
# 
# :::{note}
# This example illustrates how economics alone may not be the best decision guide, it would be kind of dumb to deny agriculture an allocation if everyone would starve. Thus a policy override might be to always provide agriculture with at least 1 unit, or artificially value agricultural allocation more.
# :::

# ## Exercises
# 
# 1. Determine the required penalty to ensure at least 1 unit of water is delivered to the agricultural sector. Interpret the results of your solution.
# 2. Suppose there is a fourth user, the in-stream requirement to ensure health of the stream itself. If the in-stream requirement is 1 flow unit, how does the allocation change for the original problem and for the cost-incentivized agricultural adjustment? Document the new Linear Program to accommodate the 4th user.
# 
# :::{note}
# The objective function is structured as a penalty-function, and can be used to determine "artifical" costs to assign to produce economically influenced, policy override results.
# :::

# ## References
# 
# 1. Loucks, D., Stedinger, J., and D. Haith. 1981. Water Resource Systems Planning and Analysis, Prentice-Hall, Englewood Cliffs, NJ
# 
# 2. Gill, Philip E. and Murray, Walter and Wright, Margaret H. 2019. Practical Optimization. Society for Industrial and Applied Mathematics, Philadelphia, PA http://dx.doi.org/10.1137/1.9781611975604

# In[ ]:




