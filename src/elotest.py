import os
import math as m
import array
import time
import numpy as np
from numpy import random as r
import scipy.integrate as integrate

master = []
#START_ELOs = [0.6, 0.8, 1.0, 1.2, 1.4]
SQRTPI_INV = 1/m.sqrt(m.pi)

order = list(range(0, 13))
START_ELOs = [x / 6 for x in order]
test1 = r.normal(loc=0, scale=0.1, size=10)


def main():
    # hello!
    #i = 0
    print(START_ELOs)
    for num in START_ELOs:
        #rand = r.normal(loc=1, scale=0.075)
        # print(rand)
        master.append(normal(num) * 1400)
        # master.append(START_ELOs[i])
        #i += 1
    print("Starting array: " + str(master))
    # print(test2)
    test()
    print(test1)
    test1[:] = [normal(x) for x in test1]
    print(test1)
    test1[:] = [3000*t for t in test1]
    test1.sort()
    print(test1)
    print(np.mean(test1))
#    print("Actual: " + str(prob_win(1400, 1600)))
    E = 1/(1 + 10**((1600 - 1400)/400))
    print("Calculated: " + str(E))
    #print("Distribution: " + str(np.mean([r.rand() for i in range(1000)])))

# def prob_win(Ra, Rb): # returns probability of win for A
#    try:
#        return ((1/700)*((Ra - Rb)) + 0.5)*(1 + r.rand()/8)
#    except ZeroDivisionError:
#        return 0.5


def normal(x):
    return (0.5 + SQRTPI_INV * float(integrate.quad(lambda t: m.exp(-(t**2)), 0, x)[0]))


def test():
    print("test\n")
    #t_start = time.time()
    #i = 0
    # while (i < 1000):
    #    test = play_game(1400, 1300)
    #    i = i + 1
    #t_end = time.time()
    test = play_game(1400, 1300)
    print(str(test[0]) + " = Ra new \n" + str(test[1]) + " = Rb new\n")
    #print(str(t_end - t_start) + " millis")


def prob(Ra, Rb):
    Ea = 1/(1 + 10**((Rb - Ra)/400))
    Eb = 1/(1 + 10**((Ra - Rb)/400))
    return (Ea, Eb)


def update_elo(Ra, Rb, result, Ea, Eb):  # if result = 1: A won, and if result = -1: B won
    temp = []
    #Ea = 1/(1 + 10**((Rb - Ra)/400))
    #Eb = 1/(1 + 10**((Ra - Rb)/400))
#    Ea, Eb = prob(Ra, Rb)[0], prob(Ra, Rb)[1]
    if (result == 1):
        a_res = 1
        b_res = 0
    elif (result == -1):
        a_res = 0
        b_res = 1
    else:
        raise ValueError("result was not -1 or 1")
    Ra_new = Ra + 32*(a_res - Ea)
    Rb_new = Rb + 32*(b_res - Eb)
    temp.append(Ra_new)
    temp.append(Rb_new)
    return temp


def play_game(Ra, Rb):
    result = r.rand()
    Ea, Eb = prob(Ra, Rb)[0], prob(Ra, Rb)[1]
    if (result <= Ea):
        result = 1
    else:
        result = -1
    return update_elo(Ra, Rb, result, Ea, Eb)


if __name__ == "__main__":
    main()
