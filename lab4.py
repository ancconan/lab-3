
s = 0
for n in range(1, 51):
    s += ( 2*n**n-1 ) / ( 2*n**n+1 )
print("4.", s)

from math import *
p = 1
for n in range(1,21):
    p*=(-1)**n*( 2*n+1 ) / ( gamma((1.45*n+1)+1)) * cos(n/2)
print("5.", p)
