# Make Influence Table for LP Soultion to Groundwater Allocation Problem
rm(list=ls())
zz <- file("influence-matrices-out.txt", "r") # Open a connection named zz to file named input.dat
# influence-matrices contain 26 tables, each 7X7+label
# ignore the first 8 rows, then capture the rest.
alist <-character(0)
amatrix <- array(0,dim=c(7,7,25))
bmatrix <- array(0,dim=c(25,25))
label <-readLines(zz, n = 1, ok = TRUE, warn = TRUE,encoding = "unknown", skipNul = FALSE)
dummy <-readLines(zz, n = 7, ok = TRUE, warn = TRUE,encoding = "unknown", skipNul = FALSE)
for (i in 1:25){
  label <-readLines(zz, n = 1, ok = TRUE, warn = TRUE,
                               encoding = "unknown", skipNul = FALSE) #clobber the existing label
  alist <-readLines(zz, n = 7, ok = TRUE, warn = TRUE,encoding = "unknown", skipNul = FALSE)
# split the list
  temparray<-as.numeric(unlist(strsplit(alist,split=",")))
# convert into a matrix
  temparray <- matrix(temparray,nrow=7,ncol=7,byrow = TRUE)
# now move temp array into the big array
  for (j in 1:7){
    for (k in 1:7){
      amatrix[j,k,i] <- temparray[j,k];
    }
  }
}
close(zz)
# split the list
# rearrange the result into 49X49 array
for (ipump in 1:25){
  icell <- 0
  for (j in 6:2){
    for(i in 2:6){
      icell <-icell+1
      bmatrix[icell,ipump] <- amatrix[i,j,ipump]
      }
  }
}
# write the result
outfile <- file("influence-table-output.txt","w")
write(bmatrix,file=outfile,ncolumns=25,sep=",")
close(outfile)


