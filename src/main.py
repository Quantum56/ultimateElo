import os
import numpy as np
from numpy import random as r
from tools import helpers as h
from tools import tournament as t
import Player as P

#START_ELOS = r.normal(loc=0, scale=0.1, size=10)
#START_ELOS[:] = [3000*h.normal(x) for x in START_ELOS]
START_ELOS = []
current_order = []

def main():
    #START_ELOS[:] = [3000*h.normal(x) for x in START_ELOS]
    # START_ELOS.sort()
    START_ELOS = h.gen_elos(16)
    START_ELOS.sort()
    print(START_ELOS)
    current_order = t.generate_tournament(16)
    print(current_order)
    p1 = P.Player(1, 1200)
    print(p1.get_rating())
    print(p1.get_rank())
    p1.set_rank(2)
    print(p1.get_rank())
    #h.test()


if __name__ == '__main__':
    main()
