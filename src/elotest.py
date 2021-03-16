import os
import math as m
import array
import time
from numpy import random as r

master = []
START_ELOs = [0.6, 0.8, 1.0, 1.2, 1.4]

test2 = list(range(0, 12))
test2[:] = [x / 6 for x in test2]

def main():
    # hello!
    i = 0
    for num in START_ELOs:
        rand = r.normal(loc=1, scale=0.075)
        print(rand)
        START_ELOs[i] = num * rand * 1400 
        master.append(START_ELOs[i])
        i += 1
    print(master)
    print(test2)
    test()


def test():
    print("test\n")
    t_start = time.time()
    i = 0
    while (i < 1000):
        test = update_elo(1400, 1200, -1)
        i = i + 1
    t_end = time.time()
    print(str(test[0]) + " = Ra new \n" + str(test[1]) + " = Rb new\n")
    print(str(t_end - t_start) + " millis")


def update_elo(Ra, Rb, result): # if result = 1: A won, and if result = -1: B won
    temp = []
    Ea = 1/(1 + 10**((Rb-Ra)/400))
    Eb = 1/(1 + 10**((Ra-Rb)/400))
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

if (__name__ == "__main__"):
    main()