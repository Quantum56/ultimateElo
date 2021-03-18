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
players = []

NUM_PlAYERS = 16


def main():
    #START_ELOS[:] = [3000*h.normal(x) for x in START_ELOS]
    # START_ELOS.sort()
    START_ELOS = h.gen_elos(NUM_PlAYERS)
    START_ELOS.sort()
    print(START_ELOS)
    current_order = t.generate_tournament(NUM_PlAYERS)
    print(current_order)
    i = 0
    for elo in START_ELOS:
        players.append(P.Player(i, elo))
        i += 1
    del i
    for player in players:
        print(str(player.id) + " -> " + str(player.rating))
    #p1 = P.Player(1, 1200)
    # print(p1.id)
    # print(p1.rating)
    #p1.rating = 1040
    # print(p1.rating)
    # h.test()
    result = h.play_game(players[0].rating, players[1].rating)
    print(str(result) + "\nPlayer " +
          str(players[0].id) + " played player " + str(players[1].id))
    if(result[1] == -1):
        print("and lost")
    else:
        print("and won")

if __name__ == '__main__':
    main()
