#!/usr/bin/env python
# coding: utf-8

# # Optimization Modeling for Decision Support

# Most engineering problems have multiple workable solutions (called feasible solutions).  Usually we apply some metric (measurement) of fitness (such as cost, weight, yield, $\dots$ , or a linear or nonlinear combination of multiple measures) that distinguish one solution from another.  If a particular solution requires time-travel, that would be infeasible (circa 2022) and removed from consideration without bothering to determine its fitness in the other measures.
# 
# The mathematical expression of fitness is called the *objective function* (also *merit function*, *cost function*, *performance function* are some other frequently appearing names for the same thing - a measure of how "good" the solution is!).  The supporting conditions, conservation laws, capacity restrictions, or other technical limitations that must be satisfied are called *constraints* (or *design requirements*, *feasibility conditions*, *auxiliary conditions*) 
# 
# When selecting an optimal solution (or non-inferior solution) we seek design values that minimize or maximize the *objective function* while simultaneously satisfying all the *constraints*.
# 
# :::{note}
# Our least-squares regression analysis that led to the normal equations in line fitting is an example of an optimization problem.  The objective function was the SSE, the constraints were mostly that the $\beta_i$'s are real valued numbers.  This is an example of unconstrained optimization - a valuable subset of the overall optimization process.
# :::
# 
# For example, suppose we want to determine the lightest weight bridge that will satisfy a given set of design requirements.  The objective function is the bridge weight expressed in terms of the dimensions of the structural elements.  The constraints will be various force and moment relationships that must be satisfied (we want the bridge to actually work!). A typical problem is to determine the dimensions of the structural elements that will minimize the weight of the bridge, subject to the appliciable constraints.  Such problems are known as optimization problems and solutions are found using mathematical programming.
# 
# Generally speaking solving linear and non-linear programming problems is relatively straightforward (given the right packages) but the formulation of the problem requires considerable care.  
# 
# :::{warning}
# Recall in our problem solving process, the problem statement was a first step to success - in mathematical programming it is a vital step, and if done haphazardly the program will fail, when the actual problem has a solution. Development of the skill to deal with such an outcome is largely experience based - the abstraction process is also vital here.
# :::

# ## Optimization Problem Characteristics
# 
# An optimization problem is written using the following logic.
# 
# Find values of the independent (*design, policy, or decision are other common names for these variables*) variables $x_1,x_2,\dots,x_n$ that will minimize (or maximize) the objective function $y=f(x_1,x_2,\dots,x_n)$.
# 
# The resulting solutions must also satisfy one or more constraint conditions usually expressed as equations or inequalities as:
# 
# $g_{eq;j}(x_1,x_2,\dots,x_n) = 0$ <br>
# $g_{le;j}(x_1,x_2,\dots,x_n) \le 0$ <br>
# $g_{ge;j}(x_1,x_2,\dots,x_n) \ge 0$ <br>
# 
# for $j=1,2,\dots,m$ where $m$ is the total number of constraints.
# 
# In addition, the permissible values of the independent variables are usually restricted to be non-negative as,
# 
# $x_i \ge 0~\text{for}~~i=1,2,\dots,n$
# 
# A further constraint, common in logistics problems is that the independent variables are integer.  
# 
# :::{warning}
# Optimization problems that are integer constrained are difficult to solve elegantly.  Don't be fooled into thinking that a real-valued solution rounded to the nearest integer is "optimal"; it might not even be feasible. It is a reasonable hack to get started, and often is a good enough approximation - just check that the result is at least feasible before commiting to the solution.
# :::
# 

# ## Useful Optimization Jargon
# 
# ### Functions
# 
# Functions map a relationship between input(s) and output(s)
# 
# Functions can be of many types:
# - Mathematical, logical, rule-based
# - The mapping of inputs => outputs can be linear or nonlinear
# - The function can be one-dimensional or multi-dimensional; the inputs can similarily be univariate (one dimension) or multivariate (many dimensions)
# 
# ### Optima
# 
# Optimization means finding either a ‘maximum’ or a ‘minimum’ of a function. The optimum value is typically defined over a range of interest.
# 
# <figure align="center">
# <!--<img src="./convexplot.png" width="300" >-->
# <img src="http://54.243.252.9/ce-5319-webroot/ce5319jb/lessons/lesson10/optima.png" width="300" >
# <figcaption>Figure X: Optima of some function </figcaption>
# </figure>
# 
# A local maximum occurs when its value is higher than other values in the vicinity; A local minimum occurs when its value is lower than other values in the vicinity. The global maximum is the largest value in the range (a,b); The global minimum is the smallest value in the range (a,b).  A Saddle Point Occurs when the value of the function is higher on one side and lower on the other (the slope and curvature are zero at the point)
# 
# ### Convex
# 
# A function is said to be strictly convex when a line connecting any two points of the function lies strictly above the function
# 
# <figure align="center">
# <!--<img src="./convexplot.png" width="300" >-->
# <img src="http://54.243.252.9/ce-5319-webroot/ce5319jb/lessons/lesson10/convexplot.png" width="300" >
# <figcaption>Figure X: Convex Function </figcaption>
# </figure>
# 
# A function is convex if the second derivative is greater than or equal 0
# 
# $$ \frac{\partial ^2 f}{\partial x} \ge 0$$
# 
# Strictly convex if greater than
# 
# $$ \frac{\partial ^2 f}{\partial x} \gt 0$$
# 
# ### Concave
# 
# A function is concave function when a line joining any two points lies below the function
# The second derivative of a concave
# 
# <figure align="center">
# <!--<img src="./concaveplot.png" width="300" >-->
# <img src="http://54.243.252.9/ce-5319-webroot/ce5319jb/lessons/lesson10/concaveplot.png" width="300" >
# <figcaption>Figure X: Concave Function </figcaption>
# </figure>
# 
# A function is concave if the second derivative is greater than or equal 0
# 
# $$ \frac{\partial ^2 f}{\partial x} \le 0$$
# 
# Strictly concave if less than
# 
# $$ \frac{\partial ^2 f}{\partial x} \lt 0$$
# 
# ### Global Optimum Values
# 
# ### Local Optimal Values
# 
# 

# In[ ]:




