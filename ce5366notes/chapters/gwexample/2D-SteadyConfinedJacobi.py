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
        #print(ir,new_list[ir][:])
        print(new_list[ir][:])
    return()
verbose = False
echoinput = False
infile = input()
print(infile)
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
        qrat[irow][jcol] = (pumping[irow][jcol])/(deltax*deltay)/365.0
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
            head[irow][jcol]=( -qrat[irow][jcol] \
+amat[irow][jcol]*head[irow-1][jcol  ] \
+bmat[irow][jcol]*head[irow+1][jcol  ] \
+cmat[irow][jcol]*head[irow  ][jcol-1] \
+dmat[irow][jcol]*head[irow  ][jcol+1] )\
            /(amat[ irow][jcol ]+ bmat[ irow][jcol ]+ cmat[ irow][jcol ]+ dmat[ irow][jcol ])

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
#        print("Exit iterations in velocity potential because tolerance met ")
#        print("Iterations =" , iter+1 ) ;
        tolflag = True
        break
    # update    
    headold = update(head,headold)
# next iteration

#print("End Calculations")
#print("Iterations    = ",iter+1)
#print("Closure Error = ",round(percentdiff,3))
# special messaging to report min head to adjust pump rates
import numpy
b = numpy.array(head)
#print("Minimum Head",round(b.min(),3))
#
#print("Head Map")
#print("----")
#writearray(head)
#print("----")
outfile = infile.strip(".txt") + '.out'
localfile = open(outfile,"w") # connect and read file for 2D gw model
localfile.writelines(outfile+'\n')
for row in range(len(head)):
    localfile.write(" ".join(map(str,head[row]))+"\n")
localfile.close()
