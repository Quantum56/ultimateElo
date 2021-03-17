import math as m
import numpy as np
from numpy import random as r
import scipy.integrate as integrate

SQRTPI_INV = 1/m.sqrt(m.pi)

def normal(x):
    return (0.5 + SQRTPI_INV * float(integrate.quad(lambda t: m.exp(-(t**2)), 0, x)[0]))

def test():
    print("test\n")
    test = play_game(1400, 1300)
    print(str(test[0]) + " = Ra new \n" + str(test[1]) + " = Rb new\n")

def prob(Ra, Rb):
    Ea = 1/(1 + 10**((Rb - Ra)/400))
    Eb = 1/(1 + 10**((Ra - Rb)/400))
    return (Ea, Eb)

def update_elo(Ra, Rb, result, Ea, Eb): # if result = 1: A won, and if result = -1: B won
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
    return (Ra_new, Rb_new)

def play_game(Ra, Rb):
    result = r.rand()
    Ea, Eb = prob(Ra, Rb)[0], prob(Ra, Rb)[1]
    if (result <= Ea):
        result = 1
    else:
        result = -1
    return update_elo(Ra, Rb, result, Ea, Eb)

if __name__ == "__main__":
    t = play_game(1400, 1300)
    print("New Ra: " + str(t[0]))
    print("New Rb: " + str(t[1]))