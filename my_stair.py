import sys

n = int(sys.argv[1])
for k in range(n):
    print( (n-k-1)*' ' + (k+1)*'#' )
