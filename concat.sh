#!/bin/bash
#Example for using loops in shell 
varname="u v w theta u2 v2 w2 T2 u3 v3 w3 u4 v4 w4 uw vw uv wT txx txy txz tyz tzz tyy csopt2 dsopt2 sgst3 phim phih"

#Nested for loop for removing the time stamp and deleting the files with time stamp 
for var in $varname 
do
for np in $(seq -f "%03g" 000 1 239)  
  do
   cp tavg_${var}_c${np}_00230000.dat tavg_${var}_c${np}.dat  
   rm tavg_${var}_c${np}_00230000.dat 
  done 
done 

#Concatenates a bunch of files 
for var in $varname 
do 
 cat tavg_${var}_c*.dat > tavg_${var}.dat 
 rm tavg_${var}-c*.dat 
done 
