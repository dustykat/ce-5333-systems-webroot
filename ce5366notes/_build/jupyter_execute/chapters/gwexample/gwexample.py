#!/usr/bin/env python
# coding: utf-8

# # Groundwater Water Allocation by Simulation-Optimization

# This chapter demonstrates pumping allocation based on total demands for consump- tion and availability of water for the certain aquifer, and an example of a ground- water simulation-optimization activity. The optimization model is created using linear programming for aquifer management to minimize the cost of the pumping and conveyance to a customer, to meet a water demand requirement, with constraints designed to prevent contaminated lake water from encroaching into the aquifer. The chapter is presented as a case study for a simple example to illustrate the organizational and computational steps involved.
# 
# ## Example (Bear 1979 pp.505-509)
# 
# shows a plan view of the aquifer system being examined. The 10 km 10 km square aquifer is divided into 25 cells of (2km 2km each). Well fields in each cell are assumed to behave as if all pumping occurs at the cell centroid, and the resulting heads are averaged throughout the cell.
# The aquifer has impervious boundaries on three sides and a lake is on the forth side. 
# The lake water quality is poor, so keeping the water level of the aquifer above a certain level should be taken into consideration to prevent water encroaching from the lake into the aquifer. 
# Therefore, water level at the distance of 1 km and 3 km from the lake should be maintained at +0.64 m and +0.95 m respectively, where the lake level is the datum (+0.0 m).
# 
# Precipitation with a rate of $N = 100 mm/yr$ is replenishing the aquifer uniformly over the entire area. The entire replenishment drains through the aquifer into the lake. The aquifer is a homogeneous-isotropic aquifer and has a transmissivity of $T = 1000 m^2/day$.
# 
# ![](aquiferplan.png)
# 
# A single consumer (city) exists in Cell 18, with a demand of 7.0$Mm^3/yr$. The cost to pump water and deliver to Cell 18 is (\$1.00 + \$0.50/km))/$Mm^3$
# The distance from a pumping cell to cell 18 expressed in cartesian coordinates is $D_i−>18 = \sqrt{(x_i − x_{18})^2 + (y_i − y_{18})^2}$ where the x and y values are the coordinates to the cell centers in kilometers (using the lower right corner is the coordinate system origin). 
# 
# For example:
# 
# - The cost to pump $1~Mm^3$ of water from Cell 18 is \$1.00,
# - The cost to pump $1~Mm^3$ water from Cell 3 and transport it to Cell 18 is \$1.00 + \$3.00 = \$4.00. The first monetary unit is the pumping cost and the remainder is the transport cost to deliver water to Cell 18.
# 
# The management objective is to supply the demand at Cell 18 at minimum cost, while maintaining the minimal water levels in Cells 16 – 25 to protect the water quality of the aquifer (and prevent lake water from entering the aquifer).
# 
# To construct the management model we can first specify the decision variables which are $P_i$ the pumping rate in $M m^3$ in the i − th cell. Then we need to specify the cost function
# 
# $$ C = \sum_{i=1}^{25}(1+[\sqrt{(x_i − x_{18})^2 + (y_i − y_{18})^2}] )\times P_i $$
# 
# Next is the influence on the aquifer heads (or drawdown) at location i caused by unit pumping at location j. These will form the various constraint equations. There are 25 cells in the aquifer that can have pumping, and 10 cells with restrictive constraints (the drawdown requirements).
# 
# The pumping decisions affect the aquifer head, so a tool to estimate the response to the decision variables is created using a computer model of the aquifer. In the example, the system is to be operated at steady conditions and the aquifer is a homogeneous-isotropic confined aquifer, so the effect of one unit of pumping at a location can be determined external to the optimization process. First, one needs to develop a groundwater hydraulic model of the system.

# ### Step 1 - Build a Useable Groundwater Flow Model
# 
# Using concepts in [Cleveland, T. G. (2023) Groundwater Models in *notes to accompany CE 4363*](http://54.243.252.9/ce-4363-webroot/ce4363notes/_build/html/lessons/groundwatermodels/13gwmodels.html#) a useable groundwater model for this example is listed below:
# 
# A typical input file is shown below:
# 
# ```
# 2000
# 2000
# 1
# 7
# 7
# 1e-29
# 900
# 1 2 3 4 5 6 7 
# 1 2 3 4 5 6 7 
# 1 0 0 0 0 0 0
# 1 0 0 0 0 0 0
# 1 1 1 1 1 1 1
# 0 0 0 0 0 0 0
# 0 2.795639 7.1792 10.46687 12.65865 13.75454 13.75454
# 0 2.795639 7.1792 10.46687 12.65865 13.75454 13.75454
# 0 2.795639 7.1792 10.46687 12.65865 13.75454 13.75454
# 0 2.795639 7.1792 10.46687 12.65865 13.75454 13.75454
# 0 2.795639 7.1792 10.46687 12.65865 13.75454 13.75454
# 0 2.795639 7.1792 10.46687 12.65865 13.75454 13.75454
# 0 2.795639 7.1792 10.46687 12.65865 13.75454 13.75454
# 2920.0 1000.0 1000.0 1000.0 1000.0 1000.0 1000.0
# 2920.0 1000.0 1000.0 1000.0 1000.0 1000.0 1000.0
# 2920.0 1000.0 1000.0 1000.0 1000.0 1000.0 1000.0
# 2920.0 1000.0 1000.0 1000.0 1000.0 1000.0 1000.0
# 2920.0 1000.0 1000.0 1000.0 1000.0 1000.0 1000.0
# 2920.0 1000.0 1000.0 1000.0 1000.0 1000.0 1000.0
# 2920.0 1000.0 1000.0 1000.0 1000.0 1000.0 1000.0
# 2920.0 1000.0 1000.0 1000.0 1000.0 1000.0 1000.0
# 2920.0 1000.0 1000.0 1000.0 1000.0 1000.0 1000.0
# 2920.0 1000.0 1000.0 1000.0 1000.0 1000.0 1000.0
# 2920.0 1000.0 1000.0 1000.0 1000.0 1000.0 1000.0
# 2920.0 1000.0 1000.0 1000.0 1000.0 1000.0 1000.0
# 2920.0 1000.0 1000.0 1000.0 1000.0 1000.0 1000.0
# 2920.0 1000.0 1000.0 1000.0 1000.0 1000.0 1000.0
# -4E05 -4E05 -4E05 -4E05 -4E05 -4E05 -4E05
# -4E05 -4E05 -4E05 -4E05 -4E05 -4E05 -4E05
# -4E05 -4E05 -4E05 -4E05 -4E05 -4E05 -4E05
# -4E05 -4E05 -4E05 -4E05 -4E05 -4E05 -4E05
# -4E05 -4E05 -4E05 -4E05 -4E05 -4E05 -4E05
# -4E05 -4E05 -4E05 -4E05 -4E05 -4E05 -4E05
# -4E05 -4E05 -4E05 -4E05 -4E05 -4E05 -4E05
# ```

# In[1]:


def sse(matrix1,matrix2):
    sse=0.0
    nr=len(matrix1) # get row count
    nc=len(matrix1[0]) # get column count
    for ir in range(nr):
        for jc in range(nc):
            sse=sse+(matrix1[ir][jc]-matrix2[ir][jc])**2
    return(sse)

def update(matrix1,matrix2):
    nr=len(matrix1) # get row count
    nc=len(matrix1[0]) # get column count
    ##print(nr,nc)
    for ir in range(nr):
        for jc in range(nc):
            ##print(ir,jc)
            matrix2[ir][jc]=matrix1[ir][jc]
    return(matrix2)

def writearray(matrix):
    nr=len(matrix) # get row count
    nc=len(matrix[0]) # get column count
    import numpy as np
    new_list = list(np.around(np.array(matrix), 6))    
    for ir in range(nr):
        print(ir,new_list[ir][:])
    return()
verbose = False
echoinput = False
infile = "base-case.txt"
localfile = open(infile,"r") # connect and read file for 2D gw model
deltax = float(localfile.readline())
deltay = float(localfile.readline())
deltaz = float(localfile.readline())
nrows = int(localfile.readline())
ncols = int(localfile.readline())
tolerance = float(localfile.readline())
maxiter = int(localfile.readline())
distancex = [] # empty list
distancex.append([float(n) for n in localfile.readline().strip().split()])
distancey = [] # empty list
distancey.append([float(n) for n in localfile.readline().strip().split()])
boundarytop = [] #empty list
boundarytop.append([float(n) for n in localfile.readline().strip().split()])
boundarybottom = [] #empty list
boundarybottom.append([int(n) for n in localfile.readline().strip().split()])
boundaryleft = [] #empty list
boundaryleft.append([int(n) for n in localfile.readline().strip().split()])
boundaryright = [] #empty list
boundaryright.append([int(n) for n in localfile.readline().strip().split()])
head =[] # empty list
for irow in range(nrows):
        head.append([float(n) for n in localfile.readline().strip().split()])
#writearray(head)
hydcondx = [] # empty list
for irow in range(nrows):
        hydcondx.append([float(n) for n in localfile.readline().strip().split()])
#writearray(hydcondx)
hydcondy = [] # empty list
for irow in range(nrows):
        hydcondy.append([float(n) for n in localfile.readline().strip().split()])
#writearray(hydcondy)
pumping = [] # empty list
for irow in range(nrows):
        pumping.append([float(n) for n in localfile.readline().strip().split()])
#writearray(pumping)
localfile.close() # Disconnect the file
##
if echoinput:
    print("--Echo Inputs--")
    print("--head--")
    writearray(head)
    print("--Kx--")
    writearray(hydcondx)
    print("--Ky--")
    writearray(hydcondy)
    print("pumping-recharge")
    writearray(pumping)
    print()
##
amat = [[0 for j in range(ncols)] for i in range(nrows)]
bmat = [[0 for j in range(ncols)] for i in range(nrows)]
cmat = [[0 for j in range(ncols)] for i in range(nrows)]
dmat = [[0 for j in range(ncols)] for i in range(nrows)]
qrat = [[0 for j in range(ncols)] for i in range(nrows)]
## Transmissivity Arrays
for irow in range(1,nrows-1):
    for jcol in range(1,ncols-1):
        amat[irow][jcol] = (( hydcondx[irow-1][jcol  ]+ hydcondx[irow  ][jcol  ]) * deltaz ) /(2.0*deltax**2)
        bmat[irow][jcol] = (( hydcondx[irow  ][jcol  ]+ hydcondx[irow+1][jcol  ]) * deltaz ) /(2.0*deltax**2)
        cmat[irow][jcol] = (( hydcondy[irow  ][jcol-1]+ hydcondy[irow  ][jcol  ]) * deltaz ) /(2.0*deltay**2)
        dmat[irow][jcol] = (( hydcondy[irow  ][jcol  ]+ hydcondy[irow  ][jcol+1]) * deltaz ) /(2.0*deltay**2)
## Net Pumping Array
for irow in range(nrows):
    for jcol in range(ncols):
        qrat[irow][jcol] = (pumping[irow][jcol])/(deltax*deltay)/365.
## Headold array
headold = [[0 for jc in range(ncols)] for ir in range(nrows)] #force a new matrix
headold = update(head,headold) # update
if echoinput:
    print("--before iterations--\n head")
    writearray(head)
    print("--headold--")
    writearray(headold)
    print("--qrat--")
    writearray(qrat)
    print("--amat--")
    writearray(amat)
    print("--bmat--")
    writearray(bmat)
    print("--cmat--")
    writearray(cmat)
    print("--dmat--")
    writearray(dmat)
    print("----")
    print()
tolflag = False

for iter in range(maxiter):
    if verbose:
        print("begin iteration\n head")
        writearray(head)
        print("--headold--")
        writearray(headold)
        print("--qrat--")
        writearray(qrat)
        print("----")

# Boundary Conditions

# first and last row special == no flow boundaries
    for jcol in range(ncols):
        if boundarytop[0][jcol] == 0: # no - flow at top
            head [0][jcol ] = head[1][jcol ]
        if boundarybottom[0][ jcol ] == 0: # no - flow at bottom
            head [nrows-1][jcol ] = head[nrows-2][jcol ]
# first and last column special == no flow boundaries     
    for irow in range(nrows): 
        if  boundaryleft[0][ irow ] == 0:
            head[irow][0] = head [irow][1] # no - flow at left
        if boundaryright[0][ irow ] == 0: 
            head [irow][ncols-1] = head[ irow ][ncols-2] # no - flow at right
# interior updates
    for irow in range(1,nrows-1):
        for jcol in range(1,ncols-1):
            head[irow][jcol]=( -qrat[irow][jcol] +amat[irow][jcol]*head[irow-1][jcol  ] +bmat[irow][jcol]*head[irow+1][jcol  ] +cmat[irow][jcol]*head[irow  ][jcol-1] +dmat[irow][jcol]*head[irow  ][jcol+1] )            /(amat[ irow][jcol ]+ bmat[ irow][jcol ]+ cmat[ irow][jcol ]+ dmat[ irow][jcol ])

    if verbose:
        print("end iteration\n head")
        writearray(head)
        print("--headold--")
        writearray(headold)
        print("--qrat--")
        writearray(qrat)
        print("----")           
# test for stopping iterations
##    print("end iteration")
##    writearray(head)
##    print("----")
##    writearray(headold)
    percentdiff = sse(head,headold)

    if  percentdiff <= tolerance:
        print("Exit iterations in velocity potential because tolerance met ")
        print("Iterations =" , iter+1 ) ;
        tolflag = True
        break
    # update    
    headold = update(head,headold)
# next iteration

print("End Calculations")
print("Iterations    = ",iter+1)
print("Closure Error = ",round(percentdiff,3))
# special messaging to report min head to adjust pump rates
import numpy
b = numpy.array(head)
print("Minimum Head",round(b.min(),3))
#
print("Head Map")
print("----")
writearray(head)
print("----")


# ### Step 2 - Create collection of input files to sequentially run to build up influence matrix
# 
# The influence matrix (or technological function) (Bear (1979) pp. 496, Eqn. 12-10 (and 12-11)) is constructed by running the groundwater flow model with one well at a time active at some unit rate (herein 1 $Mm^3/yr$), the outputs of these runs (25 in total) are saved then processed further below.  For large problems this process needs to be automated, one way is to adapt the model to run unattended as below, supply a control file that contains the name of the input file to use, and another control file (OS specific) to batch submit each run and collect the output.  The example herein assumed Linux and uses bash shell scripts [How to Write and Run Linux Shell Scripts](https://www.theserverside.com/blog/Coffee-Talk-Java-News-Stories-and-Opinions/run-Unix-shell-script-Linux-Ubuntu-command-chmod-777-permission-steps).  Windoze equivalents exist (see [Batch Scripts on Windows - Wikipedia](https://en.wikipedia.org/wiki/Batch_file),[How to Write Windows Batch Scripts](https://www.howtogeek.com/263177/how-to-write-a-batch-script-on-windows/). 
# 
# So first we create 25 files that are nearly identical to the above input file, but with a pump operating in one of the 25 cells, name them `pump1.txt` ... `pump25.txt`
# 
# The relevant part of `pump25.txt` is shown below
# 
# ```
# 2920.0 1000.0 1000.0 1000.0 1000.0 1000.0 1000.0
# 2920.0 1000.0 1000.0 1000.0 1000.0 1000.0 1000.0
# 2920.0 1000.0 1000.0 1000.0 1000.0 1000.0 1000.0
# -4E05 -4E05 -4E05 -4E05 -4E05 -4E05 -4E05
# -4E05 -4E05 -4E05 -4E05 -4E05 -4E05 -4E05
# -4E05 -4E05 -4E05 -4E05 -4E05 -4E05 -4E05
# -4E05 -4E05 -4E05 -4E05 -4E05 -4E05 -4E05
# -4E05 -4E05 -4E05 -4E05 -4E05 -4E05 -4E05
# -4E05  6E05 -4E05 -4E05 -4E05 -4E05 -4E05  <<<  The pump is in the cell adjacent to the lake
# -4E05 -4E05 -4E05 -4E05 -4E05 -4E05 -4E05
# ```
# 
# ### Step 3 - Create a control script to run the collection of inputs
# 
# Next a control file to convey the input file name to the program, in this case `input25.txt` 
# 
# ```
# pump25.txt
# ```
# 
# Finally a shell script to run 26 instances for the model, and collect the input `run_cases.sc`
# 
# ```
# #!/bin/bash
# # semi-colon means wait until process is completed
# python3 2D-SteadyConfinedJacobi.py < input0.txt > base-case.out;
# python3 2D-SteadyConfinedJacobi.py < input1.txt > pump1.out;
# python3 2D-SteadyConfinedJacobi.py < input2.txt > pump2.out;
# python3 2D-SteadyConfinedJacobi.py < input3.txt > pump3.out;
# python3 2D-SteadyConfinedJacobi.py < input4.txt > pump4.out;
# python3 2D-SteadyConfinedJacobi.py < input5.txt > pump5.out;
# python3 2D-SteadyConfinedJacobi.py < input6.txt > pump6.out;
# python3 2D-SteadyConfinedJacobi.py < input7.txt > pump7.out;
# python3 2D-SteadyConfinedJacobi.py < input8.txt > pump8.out;
# python3 2D-SteadyConfinedJacobi.py < input9.txt > pump9.out;
# python3 2D-SteadyConfinedJacobi.py < input10.txt > pump10.out;
# python3 2D-SteadyConfinedJacobi.py < input11.txt > pump11.out;
# python3 2D-SteadyConfinedJacobi.py < input12.txt > pump12.out;
# python3 2D-SteadyConfinedJacobi.py < input13.txt > pump13.out;
# python3 2D-SteadyConfinedJacobi.py < input14.txt > pump14.out;
# python3 2D-SteadyConfinedJacobi.py < input15.txt > pump15.out;
# python3 2D-SteadyConfinedJacobi.py < input16.txt > pump16.out;
# python3 2D-SteadyConfinedJacobi.py < input17.txt > pump17.out;
# python3 2D-SteadyConfinedJacobi.py < input18.txt > pump18.out;
# python3 2D-SteadyConfinedJacobi.py < input19.txt > pump19.out;
# python3 2D-SteadyConfinedJacobi.py < input20.txt > pump20.out;
# python3 2D-SteadyConfinedJacobi.py < input21.txt > pump21.out;
# python3 2D-SteadyConfinedJacobi.py < input22.txt > pump22.out;
# python3 2D-SteadyConfinedJacobi.py < input23.txt > pump23.out;
# python3 2D-SteadyConfinedJacobi.py < input24.txt > pump24.out;
# python3 2D-SteadyConfinedJacobi.py < input25.txt > pump25.out;
# cat base-case.out pump1.out pump2.out pump3.out pump4.out pump5.out pump6.out pump7.out pump8.out pump9.out pump10.out pump11.out pump12.out pump13.out pump14.out pump15.out pump16.out pump17.out pump18.out pump19.out pump20.out pump21.out pump22.out pump23.out pump24.out pump25.out > influence-matrices-out1.txt;
# # now kill all the intermediate files
# rm -rf base-case.out pump1.out pump2.out pump3.out pump4.out pump5.out pump6.out pump7.out pump8.out pump9.out pump10.out pump11.out pump12.out pump13.out pump14.out pump15.out pump16.out pump17.out pump18.out pump19.out pump20.out pump21.out pump22.out pump23.out pump24.out pump25.out
# ```
# 
# The shell script runs the base case and 25 pumping cases then collects output into a single file called `influence-matrices-out1.txt`  The program above has to be converted into a useable python program with just enough output to do the job, the listing is below.  You will see its pretty much identical to the Jupyter Script with the exception of
# ```
# infile = input()
# print(infile)
# ```
# which reads the input file (that contains the filename, and prints the name to the output, and a lot of the printed output is suppressed.  Here is the complete file `2D-SteadyConfinedJacobi.py`
# 
# ```
# def sse(matrix1,matrix2):
#     sse=0.0
#     nr=len(matrix1) # get row count
#     nc=len(matrix1[0]) # get column count
#     for ir in range(nr):
#         for jc in range(nc):
#             sse=sse+(matrix1[ir][jc]-matrix2[ir][jc])**2
#     return(sse)
# 
# def update(matrix1,matrix2):
#     nr=len(matrix1) # get row count
#     nc=len(matrix1[0]) # get column count
#     ##print(nr,nc)
#     for ir in range(nr):
#         for jc in range(nc):
#             ##print(ir,jc)
#             matrix2[ir][jc]=matrix1[ir][jc]
#     return(matrix2)
# 
# def writearray(matrix):
#     nr=len(matrix) # get row count
#     nc=len(matrix[0]) # get column count
#     import numpy as np
#     new_list = list(np.around(np.array(matrix), 6))    
#     for ir in range(nr):
#         print(ir,new_list[ir][:])
#     return()
# verbose = False
# echoinput = False
# infile = input()
# print(infile)
# localfile = open(infile,"r") # connect and read file for 2D gw model
# deltax = float(localfile.readline())
# deltay = float(localfile.readline())
# deltaz = float(localfile.readline())
# nrows = int(localfile.readline())
# ncols = int(localfile.readline())
# tolerance = float(localfile.readline())
# maxiter = int(localfile.readline())
# distancex = [] # empty list
# distancex.append([float(n) for n in localfile.readline().strip().split()])
# distancey = [] # empty list
# distancey.append([float(n) for n in localfile.readline().strip().split()])
# boundarytop = [] #empty list
# boundarytop.append([float(n) for n in localfile.readline().strip().split()])
# boundarybottom = [] #empty list
# boundarybottom.append([int(n) for n in localfile.readline().strip().split()])
# boundaryleft = [] #empty list
# boundaryleft.append([int(n) for n in localfile.readline().strip().split()])
# boundaryright = [] #empty list
# boundaryright.append([int(n) for n in localfile.readline().strip().split()])
# head =[] # empty list
# for irow in range(nrows):
#         head.append([float(n) for n in localfile.readline().strip().split()])
# #writearray(head)
# hydcondx = [] # empty list
# for irow in range(nrows):
#         hydcondx.append([float(n) for n in localfile.readline().strip().split()])
# #writearray(hydcondx)
# hydcondy = [] # empty list
# for irow in range(nrows):
#         hydcondy.append([float(n) for n in localfile.readline().strip().split()])
# #writearray(hydcondy)
# pumping = [] # empty list
# for irow in range(nrows):
#         pumping.append([float(n) for n in localfile.readline().strip().split()])
# #writearray(pumping)
# localfile.close() # Disconnect the file
# ##
# if echoinput:
#     print("--Echo Inputs--")
#     print("--head--")
#     writearray(head)
#     print("--Kx--")
#     writearray(hydcondx)
#     print("--Ky--")
#     writearray(hydcondy)
#     print("pumping-recharge")
#     writearray(pumping)
#     print()
# ##
# amat = [[0 for j in range(ncols)] for i in range(nrows)]
# bmat = [[0 for j in range(ncols)] for i in range(nrows)]
# cmat = [[0 for j in range(ncols)] for i in range(nrows)]
# dmat = [[0 for j in range(ncols)] for i in range(nrows)]
# qrat = [[0 for j in range(ncols)] for i in range(nrows)]
# ## Transmissivity Arrays
# for irow in range(1,nrows-1):
#     for jcol in range(1,ncols-1):
#         amat[irow][jcol] = (( hydcondx[irow-1][jcol  ]+ hydcondx[irow  ][jcol  ]) * deltaz ) /(2.0*deltax**2)
#         bmat[irow][jcol] = (( hydcondx[irow  ][jcol  ]+ hydcondx[irow+1][jcol  ]) * deltaz ) /(2.0*deltax**2)
#         cmat[irow][jcol] = (( hydcondy[irow  ][jcol-1]+ hydcondy[irow  ][jcol  ]) * deltaz ) /(2.0*deltay**2)
#         dmat[irow][jcol] = (( hydcondy[irow  ][jcol  ]+ hydcondy[irow  ][jcol+1]) * deltaz ) /(2.0*deltay**2)
# ## Net Pumping Array
# for irow in range(nrows):
#     for jcol in range(ncols):
#         qrat[irow][jcol] = (pumping[irow][jcol])/(deltax*deltay)/365.0
# ## Headold array
# headold = [[0 for jc in range(ncols)] for ir in range(nrows)] #force a new matrix
# headold = update(head,headold) # update
# if echoinput:
#     print("--before iterations--\n head")
#     writearray(head)
#     print("--headold--")
#     writearray(headold)
#     print("--qrat--")
#     writearray(qrat)
#     print("--amat--")
#     writearray(amat)
#     print("--bmat--")
#     writearray(bmat)
#     print("--cmat--")
#     writearray(cmat)
#     print("--dmat--")
#     writearray(dmat)
#     print("----")
#     print()
# tolflag = False
# 
# for iter in range(maxiter):
#     if verbose:
#         print("begin iteration\n head")
#         writearray(head)
#         print("--headold--")
#         writearray(headold)
#         print("--qrat--")
#         writearray(qrat)
#         print("----")
# 
# # Boundary Conditions
# 
# # first and last row special == no flow boundaries
#     for jcol in range(ncols):
#         if boundarytop[0][jcol] == 0: # no - flow at top
#             head [0][jcol ] = head[1][jcol ]
#         if boundarybottom[0][ jcol ] == 0: # no - flow at bottom
#             head [nrows-1][jcol ] = head[nrows-2][jcol ]
# # first and last column special == no flow boundaries     
#     for irow in range(nrows): 
#         if  boundaryleft[0][ irow ] == 0:
#             head[irow][0] = head [irow][1] # no - flow at left
#         if boundaryright[0][ irow ] == 0: 
#             head [irow][ncols-1] = head[ irow ][ncols-2] # no - flow at right
# # interior updates
#     for irow in range(1,nrows-1):
#         for jcol in range(1,ncols-1):
#             head[irow][jcol]=( -qrat[irow][jcol] \
# +amat[irow][jcol]*head[irow-1][jcol  ] \
# +bmat[irow][jcol]*head[irow+1][jcol  ] \
# +cmat[irow][jcol]*head[irow  ][jcol-1] \
# +dmat[irow][jcol]*head[irow  ][jcol+1] )\
#             /(amat[ irow][jcol ]+ bmat[ irow][jcol ]+ cmat[ irow][jcol ]+ dmat[ irow][jcol ])
# 
#     if verbose:
#         print("end iteration\n head")
#         writearray(head)
#         print("--headold--")
#         writearray(headold)
#         print("--qrat--")
#         writearray(qrat)
#         print("----")           
# # test for stopping iterations
# ##    print("end iteration")
# ##    writearray(head)
# ##    print("----")
# ##    writearray(headold)
#     percentdiff = sse(head,headold)
# 
#     if  percentdiff <= tolerance:
# #        print("Exit iterations in velocity potential because tolerance met ")
# #        print("Iterations =" , iter+1 ) ;
#         tolflag = True
#         break
#     # update    
#     headold = update(head,headold)
# # next iteration
# 
# #print("End Calculations")
# #print("Iterations    = ",iter+1)
# #print("Closure Error = ",round(percentdiff,3))
# # special messaging to report min head to adjust pump rates
# import numpy
# b = numpy.array(head)
# #print("Minimum Head",round(b.min(),3))
# #
# #print("Head Map")
# #print("----")
# #writearray(head)
# #print("----")
# print(head)
# ```

# Here's what the influce-matrices look like after the scripts above are completed (takes a minute to run all the scripts). 
# 
# ```
# base-case.txt
# [[0.0, 2.795638795084973, 7.179200423885699, 10.466871644384556, 12.658652457561686, 13.754542864038765, 13.754542864038765], [0.0, 2.7956387954203725, 7.179200424822737, 10.466871645816905, 12.658652459343806, 13.754542866000229, 13.754542864038765], [0.0, 2.7956387956800466, 7.179200425548213, 10.466871646925863, 12.658652460723562, 13.754542867518841, 13.754542865620678], [0.0, 2.7956387958690367, 7.1792004260762114, 10.46687164773296, 12.658652461727744, 13.75454286862408, 13.754542866771988], [0.0, 2.795638795991634, 7.179200426418723, 10.466871648256522, 12.658652462379155, 13.754542869341046, 13.754542867518841], [0.0, 2.7956387960514446, 7.179200426585822, 10.466871648511948, 12.658652462696956, 13.754542869690829, 13.754542867883204], [0.0, 2.7956387957423505, 7.179200425722277, 10.466871647191939, 12.65865246105461, 13.754542867883204, 13.754542867883204]]
# pump1.txt
# [[0.0, 2.465251988182108, 6.178523885726267, 8.714543250629065, 9.957907528734793, 9.623285411768402, 9.623285411768402], [0.0, 2.465251988181018, 6.178523885723221, 8.71454325062441, 9.957907528729002, 9.623285411762026, 9.623285411768402], [0.0, 2.4879835765095146, 6.259886007394686, 8.911307926447149, 10.440003512823896, 10.93249891121449, 10.932498911220659], [0.0, 2.5193701329486102, 6.365838229932572, 9.134908523976705, 10.8624092739344, 11.638317398086455, 11.638317398092473], [0.0, 2.546363642020228, 6.453297844444154, 9.304188254624004, 11.140517249880233, 12.024153598139634, 12.024153598145556], [0.0, 2.5614052760648285, 6.500910840233778, 9.39213898922635, 11.275427461852738, 12.197735735481512, 12.197735735487388], [0.0, 2.561405276065833, 6.500910840236584, 9.39213898923064, 11.275427461858076, 12.197735735487388, 12.197735735487388]]
# pump2.txt
# [[0.0, 2.487983576511657, 6.25988600740067, 8.911307926456297, 10.440003512835277, 10.932498911227015, 10.932498911227015], [0.0, 2.4879835765105587, 6.2598860073976015, 8.911307926451606, 10.44000351282944, 10.932498911220593, 10.932498911227015], [0.0, 2.496638544620077, 6.284476108261006, 8.93814384815381, 10.380313289839311, 10.329103898633779, 10.329103898639994], [0.0, 2.5149770855811058, 6.347345621906193, 9.080587657094334, 10.718111488769585, 11.318335111267508, 11.318335111273576], [0.0, 2.534411766993192, 6.413451225722143, 9.222859258578975, 10.997319485906806, 11.811899535428227, 11.811899535434193], [0.0, 2.546363642020218, 6.453297844444126, 9.304188254623963, 11.140517249880181, 12.024153598139575, 12.024153598145496], [0.0, 2.54636364202123, 6.453297844446954, 9.304188254628285, 11.140517249885558, 12.024153598145496, 12.024153598145496]]
# pump3.txt
# [[0.0, 2.519370132950678, 6.365838229938348, 9.134908523985535, 10.862409273945387, 11.638317398098549, 11.638317398098549], [0.0, 2.5193701329496068, 6.365838229935355, 9.134908523980963, 10.862409273939697, 11.638317398092287, 11.638317398098549], [0.0, 2.514977085581085, 6.347345621906135, 9.080587657094245, 10.718111488769479, 11.31833511126739, 11.31833511127345], [0.0, 2.511680178663629, 6.3320891040477, 9.026094582751679, 10.515223501806247, 10.502686035969528, 10.502686035975442], [0.0, 2.51497708558009, 6.347345621903356, 9.080587657089998, 10.718111488764192, 11.318335111261574, 11.31833511126739], [0.0, 2.5193701329475924, 6.365838229929729, 9.134908523972358, 10.862409273928995, 11.638317398080508, 11.638317398086278], [0.0, 2.5193701329485787, 6.365838229932484, 9.134908523976573, 10.862409273934237, 11.638317398086278, 11.638317398086278]]
# pump4.txt
# [[0.0, 2.5463636420233255, 6.453297844452808, 9.30418
# ...
# many more rows
# ...
# 
# ```
# 
# Were not done yet, these are head matrices, and our problem is 

# In[ ]:




