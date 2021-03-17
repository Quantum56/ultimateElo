import os
import sys
import numpy as np
from numpy import random as r
from tools import helpers as h

#START_ELOS = r.normal(loc=0, scale=0.1, size=10)
#START_ELOS[:] = [3000*h.normal(x) for x in START_ELOS]
START_ELOS = [3000 * h.normal(x) for x in r.normal(loc=0, scale=0.1, size=10)]
START_ELOS.sort()

def main():
    #START_ELOS[:] = [3000*h.normal(x) for x in START_ELOS]
    #START_ELOS.sort()
    print(START_ELOS)
    
if __name__=='__main__':
    main()
