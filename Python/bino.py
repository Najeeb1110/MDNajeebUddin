 #creating Filp a coin Using Binomial distribution
from numpy import random 
x = random.binomial(n=1,p=0.5,size=1)
if x[0]== 0:
    print('Tail')
else:
    print('Heads')
    